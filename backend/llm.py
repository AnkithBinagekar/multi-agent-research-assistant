from crewai import LLM

llm = LLM(
    model="ollama/tinyllama",
    base_url="http://localhost:11434",
    temperature=0.7
)
