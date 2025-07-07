# agents.py
from crewai import Agent
from tool import yt_tool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

# Load environment variables

load_dotenv()

# Get API key and model name from .env

groq_api_key = os.getenv("GROK_API_KEY")
groq_model = os.getenv("GROQ_MODEL_NAME", "gemma-7b-it")

# Initialize Groq LLM

groq_llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name=groq_model
)

# Blog researcher agent

blog_researcher = Agent(
    role='Blog Researcher from YouTube Videos',
    goal='Get the relevant video transcription for the topic {topic} from the provided YouTube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, and Generative AI, "
        "and providing actionable insights for blogs and research."
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=groq_llm  # Assign Groq LLM
)

# Blog writer agent
blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YouTube content',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate "
        "and educate readers by turning raw video insights into blog-ready content."
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=groq_llm  #  Assign Groq LLM
)
