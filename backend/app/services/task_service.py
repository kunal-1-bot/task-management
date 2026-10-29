
from sqlalchemy.orm import Session

from app.models import Task, User
from app.schemas import TaskCreate, TaskUpdate


def create_task(db: Session, payload: TaskCreate) -> Task:
    user = db.get(User, payload.user_id)

    if user is None:
        raise ValueError("User not found")

    task = Task(**payload.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_all_tasks(db: Session) -> list[Task]:
    return db.query(Task).order_by(Task.created_at.desc()).all()


def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return db.get(Task, task_id)


def update_task(
    db: Session,
    task_id: int,
    payload: TaskUpdate,
) -> Task | None:
    task = db.get(Task, task_id)

    if task is None:
        return None

    updates = payload.model_dump(exclude_unset=True)

    for field, value in updates.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = db.get(Task, task_id)

    if task is None:
        return False

    db.delete(task)
    db.commit()

    return True
