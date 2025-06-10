from sqlalchemy import select
from app.db.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

async def get_user(db: AsyncSession, user_id: str):
    try:
        query = select(User).where(User.id == uuid.UUID(user_id))
        result = await db.execute(query)
        return result.scalar_one_or_none()
    except Exception as e:
        print(f"Error fetching user: {str(e)}")
        return None