from typing import Literal

from pydantic import BaseModel


class ConversationCreate(BaseModel):
    business_id: int
    lead_id: int
    agent_id: int
    channel: Literal["phone", "sms", "email"]


class MessageCreate(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str