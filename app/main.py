from datetime import datetime

from fastapi import FastAPI





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


