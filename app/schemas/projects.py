from pydantic import BaseModel
from datetime import datetime  # Changed from date
from typing import List, Optional
import uuid

class ProjectSchema(BaseModel):
    id: uuid.UUID
    user_id: Optional[uuid.UUID]
    name: str
    description: Optional[str]
    github_link: Optional[str]
    live_link: Optional[str]
    tags: Optional[List[str]]
    created_at: Optional[datetime]  # Changed from date
    date_completed: Optional[datetime]  # Changed from date

    class Config:
        from_attributes = True