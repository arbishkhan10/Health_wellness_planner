from agents import function_tool
from guardrails import ProgressOutput, ProgressUpdate

@function_tool
def tracker_tool(update: ProgressUpdate) -> ProgressOutput:
    """
    Logs progress update.
    """
    print(f"[debug] Tracking progress: {update}")

    return ProgressOutput(
        update=update,
        status="Recorded"
    )