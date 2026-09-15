from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    business_id: Mapped[int] = mapped_column(
        ForeignKey("businesses.id"),
    )

    name: Mapped[str] = mapped_column(
        String(100),
    )

    system_prompt: Mapped[str] = mapped_column(
        Text,
    )

    greeting: Mapped[str] = mapped_column(
        Text,
    )

    voice: Mapped[str] = mapped_column(
        String(50),
        default="default",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )