from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("LLM_API_KEY")

# Set up summarization model
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    token=HF_TOKEN
)

# Routing function (simple keywords for now)
def classify_query(query: str) -> str:
    q = query.lower()
    if "project" in q:
        return "projects"
    elif "job" in q or "work" in q or "experience" in q:
        return "jobs"
    elif "skill" in q:
        return "skills"
    elif "education" in q or "school" in q:
        return "education"
    elif "profile" in q or "summary" in q:
        return "profile"
    return "unknown"

# Summarize data from a specific field (e.g., description)
def summarize_data(data: list, field: str = "description") -> str:
    combined = " ".join(item.get(field, "") for item in data if item.get(field))
    if not combined.strip():
        return "No content available to summarize."
    
    result = summarizer(combined, max_length=60, min_length=20, do_sample=False)
    return result[0]["summary_text"]
