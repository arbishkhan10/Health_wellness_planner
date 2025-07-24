import os
import asyncio
import streamlit as st
from dotenv import load_dotenv

from agents import RunConfig, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run_context import RunContextWrapper
from context import UserSessionContext
from hooks import MyRunHooks
from utils.streaming import stream_conversation
from agents_modules.agent_main import planner_agent

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

config = RunConfig(
    model=OpenAIChatCompletionsModel("gemini-2.0-flash", openai_client=client),
    model_provider=client,
    tracing_disabled=True
)

async def run_stream(user_input: str):
    user_context = RunContextWrapper(UserSessionContext(name="Amna", uid=123))
    hooks = MyRunHooks()

    response_area = st.empty()
    accumulated = ""

    async for chunk in stream_conversation(
        agent=planner_agent,
        user_input=user_input,
        context=user_context,
        config=config,
        hooks=hooks
    ):
        accumulated += chunk
        response_area.markdown(accumulated)


async def main():
    st.set_page_config(page_title="🏋️‍♀️ Health & Wellness Planner")
    st.title("🏋️‍♀️ Your Health & Wellness Planner Agent")
    st.write("Chat with your AI coach to get meal plans, workouts, and wellness support.")

    user_input = st.text_input(
        "You:",
        placeholder="Type something like 'I want to lose 4kg in 3 months'"
    )

    if user_input:
        await run_stream(user_input)


if __name__ == "__main__":
    asyncio.run(main())