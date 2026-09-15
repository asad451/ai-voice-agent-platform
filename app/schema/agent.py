from pydantic import BaseModel


class AgentCreate(BaseModel):
    business_id: int
    name: str
    system_prompt: str
    greeting: str
    voice: str = "default"