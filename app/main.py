from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Dict,Optional,List,Any
from datetime import datetime
import uuid 


VERSION = "1.0.0"

app = FastAPI(
    title="Memory Service",
    description="Memory service for storing and retrieving user memories",
    version=VERSION,
)
memories_store: Dict[str, Dict[str, Any]] = {}

class Memory(BaseModel):
    id: Optional[str]=None
    user_id: str
    content: str
    tags: Optional[List[str]]=[]
    created_at: Optional[datetime]=None
    updated_at: Optional[datetime]=None

class MemoryUpdate(BaseModel):
    content: Optional[str]=None
    tags: Optional[List[str]]=None

class MemoryResponse(BaseModel):
    id: str
    user_id:str
    content: str
    tags: Optional[List[str]]
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
    memory_id=str(uuid.uuid4())
    now=datetime.utcnow()
    memory_data={
        "id": memory_id,
        "user_id": memory.user_id,
        "tags": memory.tags or [],
        "content": memory.content,
        "created_at": now,
        "updated_at": now,
    }
    memories_store[memory_id]=memory_data
    return MemoryResponse(**memory_data)
@app.get("/memories/{memory_id}",response_model=MemoryResponse)
async def get_memory(memory_id: str):
    if memory_id not in memories_store:
        raise HTTPException(status_code=404, detail="Memory not found")
    else:
        return MemoryResponse(**memories_store[memory_id])
    
@app.get("/health")
async def health_check():
      
      return {
          "status": "healthy",
          "service": "memory-service",
          "version": VERSION,
          "total_memories": len(memories_store)
      }



