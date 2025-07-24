from agents import function_tool
from guardrails import MealPlanOutput

@function_tool
async def meal_planner_tool(days: int, diet_preferences: str) -> MealPlanOutput:
    """
    Async meal planner tool.
    """
    print(f"[debug] Planning {days}-day meal plan for {diet_preferences} diet")

    meals = [
        {"day": f"Day {i+1}", "meal": f"{diet_preferences} Meal {i+1}"}
        for i in range(days)
    ]

    return MealPlanOutput(days=days, meals=meals)