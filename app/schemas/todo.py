# app/schemas/todo.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.todo import Priority

# Shared properties
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Priority = Priority.low
    category: Optional[str] = None


# Schema for creating a new Todo
class TodoCreate(TodoBase):
    pass


# Schema for updating an existing Todo
class TodoUpdate(TodoBase):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[Priority] = Priority.low
    category: Optional[str] = None
    completed: Optional[bool] = False


# Schema for returning a Todo (DB object -> API output)
class TodoOut(TodoBase):
    id: int
    completed: bool
    priority: Priority
    date: datetime

    class Config:
        from_attributes = True   # 🔑 allows SQLAlchemy models to be returned as Pydantic schemas