#!/usr/bin/env python3
"""
CLI script for generating API documentation from Python code files.

Usage:
    python cli.py --file path/to/api.py
    python cli.py --file path/to/api.py --output path/to/output.json
"""

import argparse
import json
import sys
from pathlib import Path
from dotenv import load_dotenv

from autodoc.parser import extract_code
from autodoc.generator import DocGenerator


def main():
    """Main entry point for the CLI script."""
    # Load environment variables
    load_dotenv()
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Generate OpenAPI 3.0 documentation from Python API code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py --file api.py
  python cli.py --file api.py --output docs.json
        """
    )
    
    parser.add_argument(
        "--file",
        required=True,
        type=str,
        help="Path to the Python API file to analyze"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional path to save the generated documentation as JSON (default: print to console)"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Validate file exists
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: File '{args.file}' not found.", file=sys.stderr)
            sys.exit(1)
        
        print(f"Reading API code from {args.file}...", file=sys.stderr)
        
        # Extract code from file
        code = extract_code(str(file_path))
        
        print(f"Generating documentation...", file=sys.stderr)
        
        # Initialize DocGenerator and generate documentation
        doc_generator = DocGenerator()
        documentation = doc_generator.generate(code)
        
        # Handle output
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(documentation, f, indent=2)
            
            print(f"Documentation saved to {args.output}", file=sys.stderr)
        else:
            # Pretty print to console
            json_output = json.dumps(documentation, indent=2)
            print(json_output)
    
    except FileNotFoundError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Configuration Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"JSON Parsing Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {type(e).__name__}: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
