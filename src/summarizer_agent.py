import yaml
from crewai import Agent
from src.utils import call_llm

class SummarizerAgent:
    def __init__(self):
        with open("agents/summarizer_agent.yaml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config["name"],
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def summarize_papers(self, papers_md):
        prompt = (
            f"Summarize the following list of academic papers:\n{papers_md}\n\n"
            "For each paper, return:\n- Technical Summary (2–3 lines)\n"
            "- Why it matters\n- Breakthroughs introduced"
        )
        return call_llm(prompt)
