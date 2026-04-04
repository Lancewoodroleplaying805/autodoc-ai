from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from autodoc.generator import DocGenerator


# Load environment variables
load_dotenv()


# Initialize FastAPI app
app = FastAPI(
    title="API Documentation Generator",
    description="Generate OpenAPI 3.0 documentation from Python API code",
    version="1.0.0"
)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; configure as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize DocGenerator
doc_generator = None


def get_generator():
    """Get or initialize the DocGenerator instance."""
    global doc_generator
    if doc_generator is None:
        try:
            doc_generator = DocGenerator()
        except ValueError as e:
            raise HTTPException(status_code=500, detail=str(e))
    return doc_generator


# Request model
class CodeRequest(BaseModel):
    code: str


# Response model
class GenerationResponse(BaseModel):
    documentation: dict


@app.post("/generate", response_model=GenerationResponse)
async def generate_docs(request: CodeRequest):
    """
    Generate OpenAPI 3.0 documentation for the provided API code.
    
    Args:
        request: JSON request containing the 'code' field with Python API code
        
    Returns:
        A JSON response with the generated OpenAPI 3.0 documentation
        
    Raises:
        HTTPException: If code generation or parsing fails
    """
    try:
        if not request.code.strip():
            raise HTTPException(status_code=400, detail="Code cannot be empty")
        
        generator = get_generator()
        documentation = generator.generate(request.code)
        
        return GenerationResponse(documentation=documentation)
    
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid request: {str(e)}")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating documentation: {type(e).__name__}: {str(e)}"
        )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
