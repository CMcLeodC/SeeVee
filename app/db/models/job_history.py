from sqlalchemy import Column, String, Date, ARRAY, UUID, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class JobHistory(Base):
    __tablename__ = "job_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    company_name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    description = Column(String, nullable=True)
    technologies = Column(ARRAY(String), nullable=True)