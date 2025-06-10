from sqlalchemy import Column, String, DateTime, ARRAY, UUID, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    github_link = Column(String, nullable=True)
    live_link = Column(String, nullable=True)
    tags = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True, default=datetime.utcnow)
    date_completed = Column(DateTime(timezone=True), nullable=True)