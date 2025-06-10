from sqlalchemy import Column, String, Integer, UUID, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class Skill(Base):
    __tablename__ = "skills"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    proficiency = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True, default=datetime.utcnow)