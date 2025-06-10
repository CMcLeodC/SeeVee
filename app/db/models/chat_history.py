from sqlalchemy import Column, String, DateTime, UUID, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    query = Column(String, nullable=False)
    response = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=True, default=datetime.utcnow)