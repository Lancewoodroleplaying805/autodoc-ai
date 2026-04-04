"""Sample API file for testing autodoc-ai documentation generation."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    Get a user by their ID.
    
    Returns user information including ID and name.
    """
    return {"user_id": user_id, "name": "John Doe", "email": "john@example.com"}


@app.post("/users")
async def create_user(name: str, email: str):
    """
    Create a new user with the provided name and email.
    
    Returns the created user object with an auto-generated ID.
    """
    return {"user_id": 123, "name": name, "email": email, "created_at": "2026-04-04"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """
    Delete a user by their ID.
    
    Returns a confirmation message.
    """
    return {"message": f"User {user_id} deleted successfully"}
