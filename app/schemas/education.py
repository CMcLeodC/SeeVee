from pydantic import BaseModel
from datetime import datetime  # Changed from date
from typing import Optional
import uuid

class EducationSchema(BaseModel):
    id: uuid.UUID
    user_id: Optional[uuid.UUID]
    institution: str
    qualification: str
    field_of_study: Optional[str]
    start_date: datetime  # Changed from date
    end_date: Optional[datetime]  # Changed from date
    created_at: Optional[datetime]  # Changed from date

    class Config:
        from_attributes = True