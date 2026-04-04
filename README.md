# autodoc-ai

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)

Automatically generate OpenAPI 3.0 API documentation from Python code using Google Gemini AI.

## Overview

**autodoc-ai** is a developer tool that analyzes Python API code and generates comprehensive OpenAPI 3.0 documentation. It uses Google's Gemini 2.0 Flash model to understand your API endpoints and create structured, production-ready documentation.

## Features

- 🚀 Auto-generates OpenAPI 3.0 documentation
- 🤖 Powered by Google Gemini 2.0 Flash
- 📡 REST API built with FastAPI
- 💻 Command-line interface
- 🔄 JSON-based documentation
- ⚡ Fast and accurate

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Setup

1. Clone or download the project:
```bash
cd autodoc-ai
```

2. Install dependencies:
```bash
pip install fastapi uvicorn python-dotenv google-genai pydantic
```

## Environment Setup

1. Create a `.env` file in the project root:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

2. Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

## CLI Usage

### Generate documentation to console:
```bash
python cli.py --file path/to/your_api.py
```

### Save documentation to file:
```bash
python cli.py --file path/to/your_api.py --output docs.json
```

## API Usage

### Start the server:
```bash
python -m uvicorn app:app --reload
```

### Generate documentation via REST:
```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get(\"/users/{user_id}\")\nasync def get_user(user_id: int):\n    return {\"user_id\": user_id, \"name\": \"John Doe\"}"
  }'
```

### Health check:
```bash
curl http://localhost:8000/health
```

## Example Output

The tool returns OpenAPI 3.0 compliant JSON documentation:

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "User API",
    "version": "1.0.0"
  },
  "paths": {
    "/users/{user_id}": {
      "get": {
        "summary": "Get user by ID",
        "description": "Retrieve user information by their unique ID",
        "parameters": [
          {
            "name": "user_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            },
            "description": "The user's unique identifier"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "user_id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

## Project Structure

```
autodoc-ai/
├── cli.py                 # Command-line interface
├── app.py                 # FastAPI application
├── parser.py              # Code extraction utilities
├── prompts.py             # Prompt templates
├── autodoc/
│   ├── __init__.py
│   ├── generator.py       # DocGenerator class
│   └── prompts.py         # Prompt generation
├── .env                   # Environment variables (create this)
└── README.md              # This file
```

## Requirements

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `google-genai` - Google Gemini API client
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation

## License

MIT

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Support

For issues or questions, please open an issue on the project repository.
