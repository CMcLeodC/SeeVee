from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.queries.job_history import get_job_history
from app.db.queries.chat_history import save_chat_history
from app.schemas.job_history import JobHistorySchema
from app.schemas.query import QueryInput
from app.schemas.response import QueryResponse
from typing import List
import logging

app = FastAPI(title="CV Portfolio API", description="AI-powered CV query backend")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    return {"message": "Welcome to the CV Portfolio API"}

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(query_input: QueryInput, db: AsyncSession = Depends(get_db)):
    try:
        query = query_input.query.lower()
        user_id = "b4fceb51-aaf8-4de7-a209-0a38d730c61d"  # Hardcoded for single-user MVP

        # Basic query parsing (no LLM yet)
        if "recent jobs" in query or "work history" in query:
            jobs = await get_job_history(db, user_id)
            response_text = "Here are Connor's recent professional roles:"
            display_hint = "timeline"
            # Convert JobHistory to JobHistorySchema
            data = [JobHistorySchema.from_orm(job).dict() for job in jobs]
        else:
            response_text = "Sorry, I don't understand that query yet."
            display_hint = "text"
            data = []

        # Save to chat history
        await save_chat_history(db, user_id, query, response_text)

        return QueryResponse(
            response=response_text,
            data=data,
            display_hint=display_hint
        )
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        return QueryResponse(
            response="An error occurred while processing your query.",
            data=[],
            display_hint="text"
        )

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