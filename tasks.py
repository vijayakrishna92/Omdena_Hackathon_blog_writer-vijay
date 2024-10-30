from crewai import Task
from textwrap import dedent

class Tasks:
    def tasker(self, agent, topic): 
        return Task(
            description=dedent(f"""
                Write a comprehensive and engaging blog post based on the topic: {topic}, 
                without using section headings, SEO, or meta descriptions.
            """),
            expected_output=dedent(f"""
                A detailed and engaging blog post that captures the topic and resonates with the audience 
                without any section headings or SEO elements.
            """),
            agent=agent
        )