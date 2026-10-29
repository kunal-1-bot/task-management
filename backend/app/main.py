
from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database import engine
from app.routes.tasks import router as tasks_router
from app.routes.user import router as users_router

app = FastAPI(title="Task Management API")

app.include_router(tasks_router)
app.include_router(users_router)


@app.get("/")
def home():
    return {"message": "Task Management API is running"}


@app.get("/health/db")
def check_database():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {"database": "connected"}

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed. Check the database configuration.",
        )
