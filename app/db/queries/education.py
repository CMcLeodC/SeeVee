from sqlalchemy import select
from app.db.models.education import Education
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

async def get_education(db: AsyncSession, user_id: str):
    try:
        query = select(Education).where(Education.user_id == uuid.UUID(user_id)).order_by(Education.end_date.desc())
        result = await db.execute(query)
        return result.scalars().all()
    except Exception as e:
        print(f"Error fetching education: {str(e)}")
        return []