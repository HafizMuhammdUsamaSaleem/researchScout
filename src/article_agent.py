import yaml
from crewai import Agent
from src.utils import call_llm

class ArticleAgent:
    def __init__(self):
        with open("agents/article_agent.yaml", "r") as file:
            config = yaml.safe_load(file)

        self.agent = Agent(
            name=config["name"],
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
        )

    def search_articles(self, query: str):
        """Finds popular science/news articles related to the query."""
        prompt = (
            f"Find 5 high-quality popular articles (news, blogs, or articles) "
            f"related to the topic: '{query}'.\n\n"
            "For each article, return:\n"
            "- Title\n"
            "- Short Summary (2–3 sentences)\n"
            "- Source/Link\n\n"
            "Format the response in Markdown."
        )
        return call_llm(prompt)
