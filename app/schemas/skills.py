from pydantic import BaseModel
from datetime import datetime  # Changed from date
from typing import Optional
import uuid

class SkillSchema(BaseModel):
    id: uuid.UUID
    user_id: Optional[uuid.UUID]
    name: str
    category: Optional[str]
    proficiency: Optional[int]
    created_at: Optional[datetime]  # Changed from date

    class Config:
        from_attributes = True