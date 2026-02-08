import sys
from crewai import Crew
from tasks import research_task, analysis_task, write_task

def run(topic: str):
    crew = Crew(
        agents=[],
        tasks=[research_task, analysis_task, write_task]
    )

    result = crew.kickoff(
        inputs={"topic": topic}
    )

    return result

if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "Future of Artificial Intelligence"
    output = run(topic)

    print("\nFINAL REPORT:\n")
    print(output)
