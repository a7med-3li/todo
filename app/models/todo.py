from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, Enum
from app.dp.base import Base
import enum

class Priority(enum.Enum):
    low = 3
    medium = 2
    high = 1

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    priority = Column(Enum(Priority), default= Priority.low, nullable=False)
    category = Column(String, default=None, nullable=True)
    date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)