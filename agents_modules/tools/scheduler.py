# tools/scheduler.py

from agents import function_tool
from guardrails import SchedulerOutput

@function_tool
def scheduler_tool(user_name: str) -> SchedulerOutput:
    """
    Schedules weekly progress checks.
    """
    print(f"[debug] Scheduling check-in for: {user_name}")

    return SchedulerOutput(
        frequency="weekly",
        message=f"Weekly check-ins set for {user_name}"
    )