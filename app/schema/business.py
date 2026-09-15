from pydantic import BaseModel, EmailStr


class BusinessCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    phone: str | None = None