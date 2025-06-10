from sqlalchemy import select
from app.db.models.projects import Project
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

async def get_projects(db: AsyncSession, user_id: str):
    try:
        query = select(Project).where(Project.user_id == uuid.UUID(user_id)).order_by(Project.date_completed.desc())
        result = await db.execute(query)
        return result.scalars().all()
    except Exception as e:
        print(f"Error fetching projects: {str(e)}")
        return []