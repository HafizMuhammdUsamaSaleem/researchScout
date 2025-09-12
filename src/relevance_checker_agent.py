import yaml
from crewai import Agent
from src.utils import call_llm

class RelevanceCheckerAgent:
    def __init__(self):
        with open("agents/relevance_checker_agent.yaml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config["name"],
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def check_relevance(self, summarized_text, query):
        prompt = (
            f"Check the relevance of the following summarized papers to the query:\n'{query}'\n\n"
            f"{summarized_text}\n\n"
            "Return a list of papers with:\n- Relevance (Relevant/Not Relevant)\n- One-line reason"
        )
        return call_llm(prompt)
