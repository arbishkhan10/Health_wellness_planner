from agents import RunHooks
from typing import Any
class MyRunHooks(RunHooks):
    async def on_agent_start(self, agent, context, **kwargs):
        print(f"[RunHooks] Agent '{agent.name}' STARTED with context: {context}")

    async def on_agent_end(self, agent, context, **kwargs):
        print(f"[RunHooks] Agent '{agent.name}' ENDED with context: {context}")

    async def on_tool_start(self, tool, context, **kwargs):
        print(f"[RunHooks] Tool '{tool.name}' STARTED with context: {context}")

    async def on_tool_end(self, tool, context, **kwargs):
        print(f"[RunHooks] Tool '{tool.name}' ENDED with context: {context}")

    async def on_handoff(self, from_agent, to_agent, context, **kwargs):
        print(f"[RunHooks] Handoff triggered from '{from_agent.name}' TO '{to_agent.name}' with context: {context}")