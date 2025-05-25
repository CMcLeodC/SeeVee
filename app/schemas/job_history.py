from pydantic import BaseModel
from datetime import date
from typing import List, Optional
import uuid

class JobHistorySchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    company_name: str
    role: str
    start_date: date
    end_date: Optional[date]
    description: Optional[str]
    technologies: Optional[List[str]]

    class Config:
        from_attributes = True  # Allow ORM-to-Pydantic conversion