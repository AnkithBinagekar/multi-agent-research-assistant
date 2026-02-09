from crewai import Agent
from llm import llm

researcher = Agent(
    role="Researcher",
    goal="Research the given topic thoroughly",
    backstory="Expert internet researcher",
    llm=llm,
    verbose=False
)

analyst = Agent(
    role="Analyst",
    goal="Analyze research and extract insights",
    backstory="Critical thinker and analyst",
    llm=llm,
    verbose=False
)

writer = Agent(
    role="Writer",
    goal="Write a well-structured report",
    backstory="Professional technical writer",
    llm=llm,
    verbose=False
)
