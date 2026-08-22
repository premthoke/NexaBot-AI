"""
schemas.py

Pydantic models describing the shape of API requests/responses. These are
separate from backend/database/models.py (the ORM/table definitions) --
that's a deliberate separation:
  - database/models.py = what's stored in SQLite
  - schemas/schemas.py = what's sent/received over HTTP

Keeping them separate means you can, e.g., accept a password on input but
never include hashed_password in an output schema.
"""

from typing import Optional, Dict
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """What the frontend sends when the user submits a message."""

    message: str = Field(..., min_length=1, description="The user's raw chat message")
    session_id: str = Field(..., description="Groups messages into one conversation")

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Where is my order #12345?",
                "session_id": "a1b2c3d4",
            }
        }


class ChatResponse(BaseModel):
    """What the API sends back after processing a chat message."""

    reply: str
    detected_intent: Optional[str] = None
    extracted_entities: Optional[Dict[str, str]] = None
    confidence: Optional[float] = None


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True
