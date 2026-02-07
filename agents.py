from crewai import Agent
from crewai import LLM

# Local Ollama LLM
llm = LLM(
    model="ollama/tinyllama",
    base_url="http://localhost:11434"
)

researcher = Agent(
    role="Researcher",
    goal="Research the given topic thoroughly",
    backstory="Expert internet researcher",
    llm=llm,
    verbose=True
)

analyst = Agent(
    role="Analyst",
    goal="Analyze research and extract insights",
    backstory="Critical thinker and analyst",
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Write a well-structured report",
    backstory="Professional technical writer",
    llm=llm,
    verbose=True
)
