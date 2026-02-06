from crewai import Task
from agents import researcher, analyst, writer

research_task = Task(
    description="Research this topic: {topic}",
    expected_output="Detailed research notes",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the research",
    expected_output="Key insights and summary",
    agent=analyst
)

write_task = Task(
    description="Write final report",
    expected_output="Well structured report",
    agent=writer
)
