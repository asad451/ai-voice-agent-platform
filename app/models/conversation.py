from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    business_id: Mapped[int] = mapped_column(
        ForeignKey("businesses.id"),
    )

    lead_id: Mapped[int] = mapped_column(
        ForeignKey("leads.id"),
    )

    agent_id: Mapped[int] = mapped_column(
        ForeignKey("agents.id"),
    )

    channel: Mapped[str] = mapped_column(
        String(20),
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="active",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )