from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    text: str
    category: str
    next_action: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))