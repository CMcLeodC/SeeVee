from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.queries.job_history import get_job_history
from app.schemas.job_history import JobHistorySchema
import logging

router = APIRouter()

logger = logging.getLogger(__name__)

@router.get("/job_history", response_model=List[JobHistorySchema])
async def get_job_history_endpoint(user_id: str, db: AsyncSession = Depends(get_db)):
    try:
        jobs = await get_job_history(db, user_id)
        if not jobs:
            logger.info(f"No job history found for user_id: {user_id}")
        return jobs
    except Exception as e:
        logger.error(f"Error fetching job history: {str(e)}")
        return []
