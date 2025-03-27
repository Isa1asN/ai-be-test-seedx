# SuperCar Virtual Sales Assistant - Backend Implementation

This repository contains the implementation of a FastAPI backend for the SuperCar Virtual Sales Assistant. The backend provides a chat interface with Lex, a virtual sales assistant for SuperCar dealerships, using server-sent events (SSE) and implementing tool calling functionality with Groq API.

## Features

- Server-Sent Events (SSE) for streaming AI responses
- Integration with Groq API using llama3-70b-8192
- Tool calling for(all tools are mocked):
  - Getting weather information
  - Finding dealership addresses
  - Checking appointment availability
  - Scheduling appointments
- Conversation history tracking
- CORS handling for frontend integration

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+ (for frontend)
- Groq API key (get one at https://console.groq.com/)
    
### Running with Docker Compose (Recommended)

The easiest way to run both the backend and frontend is using Docker Compose:

1. Make sure Docker and Docker Compose are installed on your system

2. Clone this repository:
```bash
git clone https://github.com/Isa1asN/ai-be-test-seedx.git
cd ai-be-test-seedx
```

3. Set up the environment variables:
```bash
cd backend
cp .env.example .env
```

4. Edit the `.env` file with the appropriate values

5. Go to the frontend dir and create a `.env` file containing the following:
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

6. From the root directory, run:
```bash
cd infrastructure
docker-compose up
```

This will:
- Start the backend FastAPI service on http://localhost:8000
- Start the frontend Next.js application on http://localhost:3000

## API Documentation

### Endpoints

#### POST /query

Processes a user query and returns a streamed response using Server-Sent Events.

**Request Body:**
```json
{
  "query": "What is the weather in New York?",
  "session_id": "user-123"
}
```

**Response:**
The endpoint returns an event stream with the following event types:

- `chunk`: Text chunks from the AI assistant
- `tool_use`: When the AI decides to use a tool
- `tool_output`: The result of a tool execution
- `end`: Signals the end of the response stream

## Project Structure
