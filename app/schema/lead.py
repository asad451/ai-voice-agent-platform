from pydantic import BaseModel, EmailStr


class LeadCreate(BaseModel):
    name: str
    phone: str | None = None
    email: EmailStr | None = None
    notes: str | None = None