from crewai import Agent
from langchain.llms import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
mistral = HuggingFaceEndpoint(repo_id=repo_id,max_new_tokens=2048, temperature=0.3, repetition_penalty=1.1)

class ContentAgents:
    def writer_agent(self, topic):
        return Agent(
            role='Content Writer',
            goal=f'Write a detailed blog post based on the topic: {topic}',
            backstory=f"""You are a creative writer with experience in crafting engaging content on various topics. 
            Your task is to develop a compelling blog post on {topic} without section headings, SEO considerations, 
            or meta descriptions. Ensure that your writing is informative and resonates well with the target audience.""",
            llm=mistral,
            allow_delegation=False,
            verbose=True
        )