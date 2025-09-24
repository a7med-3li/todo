# app/crud/todo.py
from sqlalchemy.orm import Session
from app import models, schemas
from app.schemas import todo


# -----------------------
# CREATE
# -----------------------
def create_todo(db: Session, todo: todo.TodoCreate):
    db_todo = models.todo.Todo(
        title=todo.title,
        description=todo.description,
        priority=todo.priority,
        category=todo.category
        # completed = default False (no need to set manually)
        # created_at = handled by DB automatically
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# -----------------------
# READ (single & all)
# -----------------------
def get_todo(db: Session, todo_id: int):
    return db.query(models.todo.Todo).filter(models.todo.Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.todo.Todo).offset(skip).limit(limit).all()


# -----------------------
# UPDATE
# -----------------------
def update_todo(db: Session, todo_id: int, todo_update: todo.TodoUpdate):
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None  # Will be handled in Router

    # Only update fields provided (PATCH-style)
    update_data = todo_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo


# -----------------------
# DELETE
# -----------------------
def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None

    db.delete(db_todo)
    db.commit()
    return db_todo