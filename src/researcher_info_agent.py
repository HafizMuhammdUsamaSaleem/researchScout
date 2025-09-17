import yaml
from crewai import Agent
from src.utils import call_llm

class ResearchInfoAgent:
    def __init__(self):
        with open("agents/researcher_info_agent.yaml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config.get("name", "ResearchInfoAgent"),
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def researcher_info(self, paper_metadata, query):
        prompt = (
            f"You are tasked with enriching research papers for better context.\n\n"
            f"User Query: {query}\n\n"
            f"Paper Metadata:\n{paper_metadata}\n\n"
            "For each paper, provide:\n"
            "- A short introduction of the main researchers (2–3 lines)\n"
            "- Their primary research areas\n"
            "- A notable previous work or citation link if available\n\n"
            "Keep responses concise and factual."
        )
        return call_llm(prompt)

