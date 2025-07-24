from agents import Agent
from tools.goal_analyzer import goal_analyzer_tool
from tools.meal_planner import meal_planner_tool
from tools.workout_recommender import workout_recommender_tool
from tools.scheduler import scheduler_tool
from tools.tracker import tracker_tool

# Specialized handoff agents
from agents_modules.escalation_agent import escalation_agent
from agents_modules.injury_agent import injury_agent
from agents_modules.nutrition_agent import nutrition_agent

# 🟢 Main Health Planner Agent
planner_agent = Agent(
    
    name="HealthWellnessPlanner",
    instructions="""
    You are a digital wellness assistant.
    Help users set health goals, plan meals, suggest workouts,
    track progress, and delegate to specialists when needed.
    """,
    tools=[
        goal_analyzer_tool,
        meal_planner_tool,
        workout_recommender_tool,
        scheduler_tool,
        tracker_tool
    ],
    handoffs=[
        escalation_agent,
        injury_agent,
        nutrition_agent
    ]
)