# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from src.search_agent import SearchAgent
from src.summarizer_agent import SummarizerAgent
from src.relevance_checker_agent import RelevanceCheckerAgent

app = FastAPI()

# Load agents once
searcher = SearchAgent()
summarizer = SummarizerAgent()
relevance_checker = RelevanceCheckerAgent()

class QueryRequest(BaseModel):
    query: str

@app.post("/run-research")
def run_research(request: QueryRequest):
    query = request.query

    papers_md = searcher.search_papers(query)
    summarized = summarizer.summarize_papers(papers_md)
    relevance_result = relevance_checker.check_relevance(summarized, query)

    return {
        "papers": papers_md,
        "summaries": summarized,
        "relevance": relevance_result
    }
