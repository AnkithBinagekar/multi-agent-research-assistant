from crewai import Crew
from tasks import research_task, analysis_task, write_task

crew = Crew(
    agents=[research_task.agent, analysis_task.agent, write_task.agent],
    tasks=[research_task, analysis_task, write_task]
)

result = crew.kickoff(inputs={"topic": "Future of Artificial Intelligence"})
print(result)
