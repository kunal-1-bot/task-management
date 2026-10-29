
from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    Column,
    Date,
    ForeignKey,
    String,
    Text,
    TIMESTAMP,
    text,
)
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    user_name = Column(String(50), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=True)
    is_active = Column(
        Boolean,
        nullable=False,
        server_default=text("TRUE"),
    )
    gender = Column(String(20), nullable=True)
    date_of_birth = Column(Date, nullable=True)

    tasks = relationship(
        "Task",
        back_populates="user",
        passive_deletes=True,
    )


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    user_id = Column(
        BigInteger,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(
        String(20),
        nullable=False,
        server_default=text("'pending'"),
    )
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'in_progress', 'completed')",
            name="chk_tasks_status",
        ),
    )

    user = relationship("User", back_populates="tasks")
