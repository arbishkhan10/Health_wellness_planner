# tools/workout_recommender.py

from agents import function_tool
from guardrails import WorkoutPlanOutput

@function_tool
def workout_recommender_tool(goal: str, level: str) -> WorkoutPlanOutput:
    """
    Recommends workouts.
    """
    print(f"[debug] Recommending workouts for goal: {goal} | level: {level}")

    workouts = [
        {"exercise": "Squats"},
        {"exercise": "Push-ups"},
        {"exercise": "Planks"}
    ]

    return WorkoutPlanOutput(level=level, focus_area=goal, workouts=workouts)