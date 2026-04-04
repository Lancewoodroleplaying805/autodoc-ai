import json
import os
from dotenv import load_dotenv
import google.genai

from .prompts import get_doc_prompt


class DocGenerator:
    """A class to generate API documentation using Google's Gemini API."""
    
    def __init__(self):
        """
        Initialize the DocGenerator by loading the API key and setting up the Gemini client.
        
        Raises:
            ValueError: If GEMINI_API_KEY is not found in the environment
        """
        load_dotenv()
        
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in your .env file.")
        
        google.genai.configure(api_key=api_key)
        self.client = google.genai
    
    def generate(self, code: str) -> dict:
        """
        Generate OpenAPI 3.0 documentation for the given API code using Gemini.
        
        Args:
            code: The API code to analyze and document
            
        Returns:
            A parsed JSON dictionary containing the OpenAPI 3.0 documentation
            
        Raises:
            json.JSONDecodeError: If the response cannot be parsed as JSON
            Exception: For other API or processing errors
        """
        try:
            # Get the prompt for documentation generation
            prompt = get_doc_prompt(code)
            
            # Call the Gemini API
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            
            # Extract the text response
            response_text = response.text
            
            # Parse the JSON response
            try:
                documentation = json.loads(response_text)
                return documentation
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(
                    f"Failed to parse Gemini response as JSON: {e.msg}",
                    e.doc,
                    e.pos
                )
        
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {str(e)}")
            raise
        except Exception as e:
            print(f"Error generating documentation: {type(e).__name__}: {str(e)}")
            raise
