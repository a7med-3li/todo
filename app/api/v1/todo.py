# app/api/v1/todo.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.crud import todo as crud_todo
from app.dp.session import get_db

router = APIRouter()


# -----------------------
# CREATE
# -----------------------
@router.post("/", response_model=schemas.todo.TodoOut)
def create_todo(todo: schemas.todo.TodoCreate, db: Session = Depends(get_db)):
    return crud_todo.create_todo(db, todo)


# -----------------------
# READ (all)
# -----------------------
@router.get("/", response_model=List[schemas.todo.TodoOut])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud_todo.get_todos(db, skip=skip, limit=limit)
    return todos


# -----------------------
# READ (single)
# -----------------------
@router.get("/{todo_id}", response_model=schemas.todo.TodoOut)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud_todo.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


# -----------------------
# UPDATE
# -----------------------
@router.put("/{todo_id}", response_model=schemas.todo.TodoOut)
def update_todo(todo_id: int, todo: schemas.todo.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud_todo.update_todo(db, todo_id, todo)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


# -----------------------
# DELETE
# -----------------------
@router.delete("/{todo_id}", response_model=schemas.todo.TodoOut)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud_todo.delete_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo