from pydantic import BaseModel, Field
from typing import List, Literal

class GoalInput(BaseModel):
    """Input: Raw user goal, e.g., 'lose 4kg in 3 months'."""
    quantity: float = Field(..., description="Numeric quantity for the goal, e.g., 4")
    metric: str = Field(..., description="Measurement unit, e.g., 'kg', 'pounds'")
    duration: str = Field(..., description="Timeframe for the goal, e.g., '3 months'")
    class Config:
        extra = "forbid"
class ParsedGoal(BaseModel):
    """Parsed version of user goal for internal processing."""
    quantity: float = Field(..., description="Parsed numeric quantity")
    metric: str = Field(..., description="Parsed measurement unit")
    duration: str = Field(..., description="Parsed timeframe")
    class Config:
        extra = "forbid"
class StructuredGoal(BaseModel):
    """Final structured goal with a natural language description and parsed parts."""
    goal_description: str = Field(..., description="Human-readable goal description")
    parsed: ParsedGoal
    class Config:
        extra = "forbid"
class Meal(BaseModel):
    """Single meal item with name and calories."""
    name: str = Field(..., description="Meal name, e.g., 'Avocado Chickpea Bowl'")
    calories: str = Field(..., description="Approximate calorie content")
    class Config:
        extra = "forbid"
class MealPlanOutput(BaseModel):
    """7-day or custom meal plan output."""
    days: int = Field(..., description="Number of days covered in the plan")
    meals: List[Meal] = Field(..., description="List of meal items")
    class Config:
        extra = "forbid"
class Workout(BaseModel):
    """Single workout item with name and reps or duration."""
    name: str = Field(..., description="Workout name, e.g., 'Push-ups'")
    reps: str = Field(..., description="Reps or sets info, e.g., '2x12 reps'")
    class Config:
        extra = "forbid"
class WorkoutPlanOutput(BaseModel):
    """Personalized workout plan output."""
    level: Literal["beginner", "intermediate", "advanced"] = Field(
        ..., description="Experience level"
    )
    focus_area: str = Field(..., description="Focus area, e.g., 'legs', 'core'")
    workouts: List[Workout] = Field(..., description="List of workouts in the plan")
    class Config:
        extra = "forbid"
class SchedulerOutput(BaseModel):
    """Scheduler output for setting check-ins or reminders."""
    frequency: str = Field(..., description="How often, e.g., 'weekly', 'daily'")
    message: str = Field(..., description="Reminder message or notes")
    class Config:
        extra = "forbid"
class ProgressUpdate(BaseModel):
    """Single progress update step."""
    step: str = Field(..., description="Step description, e.g., 'Weight logged'")
    value: str = Field(..., description="Value update, e.g., '4.5kg lost'")
    class Config:
        extra = "forbid"
class ProgressOutput(BaseModel):
    """Output for tracking user progress."""
    update: ProgressUpdate
    status: str = Field(..., description="Status message, e.g., 'On track', 'Behind schedule'")
    class Config:
        extra = "forbid"