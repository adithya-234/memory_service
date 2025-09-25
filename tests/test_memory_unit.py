from uuid import uuid4
from app.main import create_memory, get_memory, memories_store


def test_create_memory():
    memories_store.clear()
    user_id = uuid4()
    content = "test memory"

    memory = create_memory(user_id, content)

    assert memory["content"] == content
    assert memory["user_id"] == user_id
    assert "id" in memory
    assert "created_at" in memory
    assert "updated_at" in memory
    assert memory["id"] in memories_store


def test_get_memory():
    memories_store.clear()
    user_id = uuid4()
    content = "test memory"

    created_memory = create_memory(user_id, content)
    memory_id = created_memory["id"]

    retrieved_memory = get_memory(memory_id)

    assert retrieved_memory is not None
    assert retrieved_memory["id"] == memory_id
    assert retrieved_memory["content"] == content
    assert retrieved_memory["user_id"] == user_id


def test_get_nonexistent_memory():
    memories_store.clear()
    nonexistent_id = uuid4()

    memory = get_memory(nonexistent_id)

    assert memory is None