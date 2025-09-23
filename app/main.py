from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional, Any
from datetime import datetime, timezone
from uuid import UUID, uuid4


VERSION = "1.0.0"

app = FastAPI(
    title="Memory Service",
    description="Memory service for storing and retrieving user memories",
    version=VERSION,
)

memories_store: Dict[UUID, Dict[str, Any]] = {}


class Memory(BaseModel):
    id: Optional[UUID] = None
    user_id: str
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))



class MemoryResponse(BaseModel):
    id: UUID
    user_id: str
    content: str
    created_at: datetime
    updated_at: datetime


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Memory Service",
        "service": "memory-service",
        "version": VERSION,
    }


@app.post("/memories", response_model=MemoryResponse)
async def create_memory(memory: Memory):
    memory_id = uuid4()
    memory_data = {
        "id": memory_id,
        "user_id": memory.user_id,
        "content": memory.content,
        "created_at": memory.created_at,
        "updated_at": memory.updated_at,
    }
    memories_store[memory_id] = memory_data
    return MemoryResponse(**memory_data)


@app.get("/memories/{memory_id}", response_model=MemoryResponse)
async def get_memory(memory_id: UUID):
    if memory_id not in memories_store:
        raise HTTPException(status_code=404, detail="Memory not found")
    return MemoryResponse(**memories_store[memory_id])


