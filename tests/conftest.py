import pytest
from fastapi.testclient import TestClient
from app.main import app, memories_store


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def clear_memories_store():
    yield
    memories_store.clear()