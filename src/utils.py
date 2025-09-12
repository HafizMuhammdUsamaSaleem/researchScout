import os
import google.generativeai as genai
from dotenv import load_dotenv

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
