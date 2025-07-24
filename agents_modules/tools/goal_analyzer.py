from agents import function_tool 
from guardrails import GoalInput, StructuredGoal 

@function_tool
def goal_analyzer_tool(goal_description: str) -> StructuredGoal:
    """
    Parses a user goal description to structured goal data.
    """
    print(f"[debug] Analyzing goal: {goal_description}")

    # Dummy parse logic for demonstration
    parsed = {
        "quantity": "4",
        "metric": "kg",
        "duration": "3 months"
    }

    return StructuredGoal(
        goal_description=goal_description,
        parsed=parsed
    )