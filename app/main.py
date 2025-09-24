# app/main.py
from fastapi import FastAPI
from app.api.v1 import todo
from app.dp.base import Base
from app.dp.session import engine

# Create all DB tables (for dev only, migrations are better for prod)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API")

# Include Routers
app.include_router(todo.router, prefix="/api/v1/todos", tags=["todos"])

from app.core.config import settings
print("DATABASE_URL loaded:", settings.DATABASE_URL)