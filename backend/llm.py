from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    base_url="http://localhost:11434"
)
