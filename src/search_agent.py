import yaml
from crewai import Agent
from src.utils import call_llm

class SearchAgent:
    def __init__(self):
        with open("agents/search_agent.yaml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config["name"],
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def search_papers(self, query):
        prompt = (
            f"Find 5 relevant academic research papers for the query:\n'{query}'.\n"
            "For each paper, include:\n"
            "- Title\n- Abstract (2-3 lines)\n- Link (correct link of paper)\n\n"
            "Return as Markdown list."
        )
        return call_llm(prompt)
