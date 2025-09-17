import os
import google.generativeai as genai
from dotenv import load_dotenv
import requests

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Pro once
model = genai.GenerativeModel("gemini-2.0-flash")

def call_llm(prompt: str) -> str:
    """Call Gemini Pro with a prompt and return the response text."""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Gemini API Error] {e}"

def validate_url(url: str) -> bool:
    """Check if a URL is publicly accessible (status 200)."""
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def filter_results(results):
    """Filter only results with valid URLs."""
    valid_results = []
    for r in results:
        if "url" in r and validate_url(r["url"]):
            valid_results.append(r)
    return valid_results
