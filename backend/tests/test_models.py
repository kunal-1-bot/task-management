from app.database import Base
from app import models


def test_models_are_registered():
    assert "users" in Base.metadata.tables
    assert "tasks" in Base.metadata.tables