from crewai import Agent

ollama_config = {
    "model": "ollama/phi3",
    "base_url": "http://localhost:11434"
}

researcher = Agent(
    role="Researcher",
    goal="Find useful information about a topic",
    backstory="Expert internet researcher",
    llm=ollama_config,
    verbose=True
)

analyst = Agent(
    role="Analyst",
    goal="Analyze and summarize research",
    backstory="Critical thinker",
    llm=ollama_config,
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Write clear final report",
    backstory="Professional writer",
    llm=ollama_config,
    verbose=True
)
