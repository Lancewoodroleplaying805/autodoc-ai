def get_doc_prompt(code: str) -> str:
    """
    Generate a prompt for an LLM to analyze API code and generate OpenAPI 3.0 documentation.
    
    Args:
        code: The API code to analyze
        
    Returns:
        A prompt string instructing the LLM to generate OpenAPI 3.0 documentation
    """
    prompt = f"""Analyze the following API code and generate comprehensive documentation in OpenAPI 3.0 JSON format.

API Code:
```
{code}
```

Generate documentation that includes:
1. **Endpoint path**: The URL path of the API endpoint
2. **HTTP method**: GET, POST, PUT, DELETE, PATCH, etc.
3. **Description**: A clear description of what the endpoint does
4. **Request parameters**: Query parameters, path parameters, and headers (if any)
5. **Request body**: The structure of the request payload (if applicable)
6. **Response format**: The structure of the successful response
7. **Example responses**: Provide 1-2 realistic example responses

Return ONLY a valid JSON object following the OpenAPI 3.0 specification. Do not include any explanatory text, markdown formatting, or content outside the JSON object. The JSON should start with {{ and end with }}.

Example OpenAPI 3.0 structure:
{{
  "openapi": "3.0.0",
  "info": {{
    "title": "API Title",
    "version": "1.0.0"
  }},
  "paths": {{
    "/endpoint": {{
      "get": {{
        "summary": "Brief description",
        "description": "Detailed description",
        "parameters": [...],
        "responses": {{
          "200": {{
            "description": "Success",
            "content": {{
              "application/json": {{
                "schema": {{...}}
              }}
            }}
          }}
        }}
      }}
    }}
  }}
}}

Now generate the OpenAPI 3.0 documentation for the provided API code. Return only valid JSON."""
    
    return prompt
