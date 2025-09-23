# Memory Service

A simple FastAPI service that allows users to store and retrieve personal memories. Think of it as a digital notepad where users can save things they want to remember and easily look them up later.

## Features

- **Memory Creation**: Store memories with content and automatic timestamp tracking
- **Memory Retrieval**: Get specific memories by ID
- **User Identification**: User-based memory storage with UUID header support
- **Service Information**: Root endpoint providing basic service details
- **In-memory storage**: Fast access with UUID-based indexing
- **RESTful API**: Clean API design with proper HTTP methods
- **Testing Infrastructure**: Comprehensive test setup with pytest and fixtures

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
- `POST /memories` - Create a new memory (requires `user-id` header)
- `GET /memories/{memory_id}` - Retrieve a specific memory by ID

### Testing

Run tests with:
```bash
pytest
```


## Project Goals

- Build a minimal but functional memory storage service
- Focus on simplicity and ease of use
- Provide reliable storage and retrieval of user memories