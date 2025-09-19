from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

class MemoryCreate(BaseModel):
    content: str
    tags: Optional[List[str]] = []

class Memory(BaseModel):
    id: str
    content: str
    tags: List[str]
    created_at: datetime
    updated_at: datetime

app = FastAPI(
    title="Memory Service",
    description="Memory service for storing and retrieving user memories",
    version="1.0.0"
)


memories_db: dict[str, Memory] = {}

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Memory Service",
        "service": "memory-service",
        "version": "1.0.0"
    }

@app.post("/memories", response_model=Memory)
async def create_memory(memory_data: MemoryCreate):
    memory_id = str(uuid.uuid4())
    now = datetime.now()

    memory = Memory(
        id=memory_id,
        content=memory_data.content,
        tags=memory_data.tags or [],
        created_at=now,
        updated_at=now
    )

    memories_db[memory_id] = memory
    return memory

@app.get("/memories", response_model=List[Memory])
async def get_all_memories():
    return list(memories_db.values())

@app.get("/memories/{memory_id}", response_model=Memory)
async def get_memory(memory_id: str):
    if memory_id not in memories_db:
        raise HTTPException(status_code=404, detail="Memory not found")
    return memories_db[memory_id]