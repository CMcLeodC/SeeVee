from sqlalchemy import select
from app.db.models.skills import Skill
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

async def get_skills(db: AsyncSession, user_id: str):
    try:
        query = select(Skill).where(Skill.user_id == uuid.UUID(user_id)).order_by(Skill.proficiency.desc())
        result = await db.execute(query)
        return result.scalars().all()
    except Exception as e:
        print(f"Error fetching skills: {str(e)}")
        return []