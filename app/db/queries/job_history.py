from sqlalchemy import select
from app.db.models.job_history import JobHistory
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

async def get_job_history(db: AsyncSession, user_id: str):
    try:
        query = select(JobHistory).where(JobHistory.user_id == uuid.UUID(user_id)).order_by(JobHistory.end_date.desc())
        result = await db.execute(query)
        return result.scalars().all()
    except Exception as e:
        print(f"Error fetching job history: {str(e)}")
        return []