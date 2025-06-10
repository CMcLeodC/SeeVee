from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import uuid

class UserSchema(BaseModel):
    id: uuid.UUID
    email: str
    name: str
    linkedin_url: Optional[str]
    github_url: Optional[str]
    phone: Optional[str]
    location: Optional[str]
    summary: Optional[str]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True