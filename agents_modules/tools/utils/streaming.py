import asyncio
from agents import Runner, Agent
from agents.run_context import RunContextWrapper
from context import UserSessionContext
from hooks import MyRunHooks
from agents import RunConfig

async def stream_conversation(
    agent: Agent,
    user_input: str,
    context: RunContextWrapper[UserSessionContext],
    config: RunConfig,
    hooks: MyRunHooks
):
    queue = asyncio.Queue()
    loop = asyncio.get_running_loop()

    def blocking_runner(future):
        # This will block until the coroutine finishes
        result = future.result()

        for event in result.stream_events:
            if event.step_type == "TOOL_START":
                chunk = f"\n🔧 [TOOL START]: {event.tool_name} with input: {event.tool_input}\n"
            elif event.step_type == "TOOL_END":
                chunk = f"\n✅ [TOOL END]: {event.tool_name} -> {event.tool_output}\n"
            elif event.step_type == "HANDOFF":
                chunk = f"\n🤝 [HANDOFF]: Delegated to {event.handoff_target}\n"
            else:
                chunk = event.pretty_output

            asyncio.run_coroutine_threadsafe(queue.put(chunk), loop)

        asyncio.run_coroutine_threadsafe(queue.put(None), loop)

    # ✅ Proper: run the coroutine on the loop
    future = asyncio.run_coroutine_threadsafe(
        Runner.run_streamed(
            starting_agent=agent,
            input=user_input,
            context=context,
            run_config=config,
            hooks=hooks
        ),
        loop
    )

    # ✅ Kick off blocking_runner in the executor with future
    loop.run_in_executor(None, blocking_runner, future)

    while True:
        chunk = await queue.get()
        if chunk is None:
            break
        yield chunk