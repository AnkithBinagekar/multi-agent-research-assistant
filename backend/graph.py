from typing import TypedDict
from langgraph.graph import StateGraph
from langchain_ollama import ChatOllama

#llm = ChatOllama(model="phi3")
llm = ChatOllama(model="tinyllama")


class State(TypedDict):
    topic: str
    research: str
    analysis: str
    report: str

def researcher(state: State):
    print(">> Researcher working...")
    result = llm.invoke(f"Research the topic: {state['topic']}")
    return {"research": result.content}

def analyst(state: State):
    print(">> Analyst working...")
    result = llm.invoke(f"Analyze this:\n{state['research']}")
    return {"analysis": result.content}

def writer(state: State):
    print(">> Writer working...")
    result = llm.invoke(f"Write report from:\n{state['analysis']}")
    return {"report": result.content}

builder = StateGraph(State)

builder.add_node("researcher", researcher)
builder.add_node("analyst", analyst)
builder.add_node("writer", writer)

builder.set_entry_point("researcher")
builder.add_edge("researcher", "analyst")
builder.add_edge("analyst", "writer")

graph = builder.compile()

print("Starting multi-agent system...")

output = graph.invoke({"topic": "Future of Artificial Intelligence"})

print("\nFINAL REPORT:\n")
print(output["report"])
