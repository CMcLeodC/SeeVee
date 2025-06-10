from pydantic import BaseModel
from typing import List, Any

class QueryResponse(BaseModel):
    response: str
    data: List[Any]
    display_hint: str