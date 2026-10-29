
from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserCreate
from app.security import hash_password, verify_password


def register_user(db: Session, payload: UserCreate) -> User:
    existing_email = (
        db.query(User)
        .filter(User.email == str(payload.email))
        .first()
    )

    if existing_email:
        raise ValueError("Email already registered")

    existing_username = (
        db.query(User)
        .filter(User.user_name == payload.user_name)
        .first()
    )

    if existing_username:
        raise ValueError("Username already taken")

    user_data = payload.model_dump(exclude={"password"})
    user_data["email"] = str(payload.email)
    user_data["password_hash"] = hash_password(payload.password)

    user = User(**user_data)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception:
        db.rollback()
        raise

def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()

    if user is None or not user.is_active:
        return None

    if not verify_password(password, user.password_hash):
        return None

