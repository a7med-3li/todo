# app/dp/base.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.todo import Todo

