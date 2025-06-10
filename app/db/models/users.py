from sqlalchemy import Column, String, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, default="Connor Clements")
    linkedin_url = Column(String, nullable=True, default="https://www.linkedin.com/in/connor-andrew-clements/")
    github_url = Column(String, nullable=True, default="https://github.com/CMcLeodC")
    phone = Column(String, nullable=True, default="659270445")
    location = Column(String, nullable=True, default="Madrid, España / Remoto")
    summary = Column(String, nullable=True, default="Profesional experimentado y fuerte comunicador motivado a mejorar...")
    created_at = Column(DateTime, nullable=True, default=datetime.utcnow)