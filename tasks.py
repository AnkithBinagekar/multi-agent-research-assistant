from crewai import Task
from agents import researcher, analyst, writer

research_task = Task(
    description="Research the topic: {topic}",
    expected_output="Detailed bullet point research notes about the topic.",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the research and summarize key insights.",
    expected_output="Clear analytical summary of main points.",
    agent=analyst
)

write_task = Task(
    description="Write a final structured report based on analysis.",
    expected_output="Well-formatted report with headings and conclusion.",
    agent=writer
)
