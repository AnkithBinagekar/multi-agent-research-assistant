from crewai import Crew
from tasks import research_task, analysis_task, write_task

crew = Crew(
    agents=[],
    tasks=[research_task, analysis_task, write_task]
)

result = crew.kickoff(
    inputs={"topic": "Future of Artificial Intelligence"}
)

print("\nFINAL REPORT:\n")
print(result)
