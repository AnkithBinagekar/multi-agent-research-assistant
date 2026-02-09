from crewai import Crew
from tasks import research_task, analysis_task, write_task
import sys
import json

def run(topic: str):
    crew = Crew(
        agents=[],
        tasks=[research_task, analysis_task, write_task],
        verbose=False
    )

    result = crew.kickoff(inputs={"topic": topic})

    # HARD CAST EVERYTHING TO STRING
    final_text = str(result)

    print(json.dumps({"final": final_text}, ensure_ascii=False))

if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "AI Research"
    run(topic)
