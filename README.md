# Memory Service

A simple service that allows users to store and retrieve personal memories. Think of it as a digital notepad where users can save things they want to remember and easily look them up later.

## Overview

The Memory Service provides a lightweight solution for personal memory management. Users can:
- **Store memories**: Add text-based memories with optional tags or categories
- **Retrieve memories**: Search and find previously stored memories
- **Organize**: Keep memories organized for easy retrieval

## Features

- Simple API for storing and retrieving memories
- Search functionality to find specific memories
- Lightweight and fast
- Easy to set up and use

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd memory_service
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, visit:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### API Endpoints

- `POST /memories` - Create a new memory
- `GET /memories` - Get all memories
- `GET /memories/{memory_id}` - Get a specific memory by ID

## Project Goals

- Build a minimal but functional memory storage service
- Focus on simplicity and ease of use
- Provide reliable storage and retrieval of user memories