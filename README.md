# Memory Service

A simple service that allows users to store and retrieve personal memories. Think of it as a digital notepad where users can save things they want to remember and easily look them up later.

## Overview


The Memory Service is a FastAPI-based web service for personal memory management. Features include:
- **Memory Creation**: Store memories with content, tags, and automatic timestamp tracking
- **Memory Retrieval**: Get specific memories by ID
- **Health Check**: Monitor service status and memory count
- **Service Information**: Root endpoint providing basic service details

## Features

- Create and store memories with unique IDs
- Retrieve memories by ID
- Tag-based memory organization
- Automatic timestamp tracking (created_at, updated_at)
- Health check endpoint
- In-memory storage for fast access
- RESTful API design

The Memory Service is a FastAPI-based web service framework for personal memory management. Currently implemented features:
- **Basic API setup**: FastAPI application with proper configuration
- **Service information**: Root endpoint providing basic service details

## Features

- Basic FastAPI application setup
- Root endpoint for service information

- Lightweight and fast

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
source venv/bin/activate
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


### API Endpoints

- `GET /` - Root endpoint that returns service information

- `POST /memories` - Create a new memory
- `GET /memories/{memory_id}` - Retrieve a specific memory by ID
- `GET /health` - Health check endpoint with service status


## Project Goals

- Build a minimal but functional memory storage service
- Focus on simplicity and ease of use
- Provide reliable storage and retrieval of user memories