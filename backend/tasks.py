from crewai import Task
from agents import researcher, analyst, writer

research_task = Task(
    description="Research the topic: {topic}",
    agent=researcher,
    expected_output="Detailed bullet point research notes"
)

analysis_task = Task(
    description="Analyze the research and summarize key insights",
    agent=analyst,
    expected_output="Clear analytical summary"
)

write_task = Task(
    description="Write a final structured report based on analysis",
    agent=writer,
    expected_output="Well-formatted report with headings and conclusion"
)
