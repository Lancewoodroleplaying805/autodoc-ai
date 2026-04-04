def extract_code(file_path: str) -> str:
    """
    Extract and return the contents of a Python file as a string.
    
    Args:
        file_path: The path to the Python file to read
        
    Returns:
        The contents of the file as a string
        
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the file cannot be read due to permission restrictions
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot read the file '{file_path}'.")
