import os
from typing import Optional

def get_openai_api_key() -> Optional[str]:
    """Get OpenAI API key from environment variable."""
    return os.getenv("OPENAI_API_KEY")

def get_langsmith_api_key() -> Optional[str]:
    """Get LangSmith API key from environment variable."""
    return os.getenv("LANGSMITH_API_KEY")

def get_langsmith_endpoint() -> str:
    """Get LangSmith endpoint from environment variable."""
    return os.getenv("LANGSMITH_ENDPOINT", "https://api.smith.langchain.com")

def get_langsmith_project() -> str:
    """Get LangSmith project from environment variable."""
    return os.getenv("LANGSMITH_PROJECT", "default") 