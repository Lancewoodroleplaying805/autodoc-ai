"""Autodoc package for API documentation generation."""

from .generator import DocGenerator
from .parser import extract_code
from .prompts import get_doc_prompt

__all__ = ["DocGenerator", "extract_code", "get_doc_prompt"]
