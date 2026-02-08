from crewai import Crew
from agents import researcher, analyst, writer
from tasks import research_task, analysis_task, write_task

def run_pipeline(topic: str):
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, write_task],
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": topic})
    return result

