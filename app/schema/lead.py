from pydantic import BaseModel, EmailStr


from pydantic import BaseModel, EmailStr


class LeadCreate(BaseModel):
    business_id: int
    name: str
    phone: str | None = None
    email: EmailStr | None = None
    notes: str | None = None