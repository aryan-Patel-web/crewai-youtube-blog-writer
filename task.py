# task.py
from crewai import Task
from tool import yt_tool
from agents import blog_researcher, blog_writer

# Research task
research_task = Task(
    description="Identify the video {topic} and get detailed information about it from the channel.",
    expected_output="A comprehensive 3-paragraph report based on the video content on {topic}.",
    tools=[yt_tool],
    agent=blog_researcher
)

# Writing task
write_task = Task(
    description="Summarize the video information on {topic} and write a blog post.",
    expected_output="A complete blog post based on the {topic} content from the YouTube channel.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)
