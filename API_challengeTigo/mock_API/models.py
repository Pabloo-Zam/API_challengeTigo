from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class MatchRule(BaseModel):
    query: Optional[Dict[str, Any]] = None
    body: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, Any]] = None

class MockConfig(BaseModel):
    id: Optional[str] = None
    path: str
    method: str
    match: Optional[MatchRule] = Field(default_factory=MatchRule)
    status_code: int = 200
    response_content: str
    content_type: str = "application/json"
