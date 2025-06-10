from sqlalchemy import insert
from app.db.models.chat_history import ChatHistory
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

async def save_chat_history(db: AsyncSession, user_id: str, query: str, response: str):
    try:
        stmt = insert(ChatHistory).values(
            user_id=uuid.UUID(user_id) if user_id else None,
            query=query,
            response=response
        )
        await db.execute(stmt)
        await db.commit()
    except Exception as e:
        print(f"Error saving chat history: {str(e)}")
        await db.rollback()