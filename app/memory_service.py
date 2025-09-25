from typing import Dict, Any
from datetime import datetime, timezone
from uuid import UUID, uuid4


class MemoryService:
    def __init__(self):
        self.memories = {}

    def create_memory(self, user_id, content):
        memory_id = uuid4()
        memory_data = {
            "id": memory_id,
            "user_id": user_id,
            "content": content,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
        }
        self.memories[memory_id] = memory_data
        return memory_data

    def get_memory(self, memory_id):
        return self.memories.get(memory_id)

    def clear_memories(self):
        self.memories.clear()