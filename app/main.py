from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.queries.job_history import get_job_history
from app.schemas.job_history import JobHistorySchema
from typing import List
import logging

app = FastAPI(title="CV Portfolio API", description="AI-powered CV query backend")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    return {"message": "Welcome to the CV Portfolio API"}

@app.post("/query")
async def query_endpoint(query: dict):
    # Placeholder for LangChain/Supabase logic
    return {
        "response": "This is a placeholder response",
        "data": [],
        "display_hint": "text"
    }

@app.get("/job_history", response_model=List[JobHistorySchema])
async def get_job_history_endpoint(user_id: str, db: AsyncSession = Depends(get_db)):
    try:
        jobs = await get_job_history(db, user_id)
        if not jobs:
            logger.info(f"No job history found for user_id: {user_id}")
        return jobs
    except Exception as e:
        logger.error(f"Error fetching job history: {str(e)}")
        return []