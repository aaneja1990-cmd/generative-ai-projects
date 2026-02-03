"""
Configuration module for loading environment variables and API keys.

This module handles loading API keys from a .env file and makes them
available to the rest of the application.
"""

import os
from dotenv import load_dotenv

def load_config():
    """
    Load environment variables from .env file.
    
    This function should be called once at the start of the application.
    It loads the API keys needed for:
    - OpenAI (for the LLM)
    - Tavily (for web search)
    - SERP API (for flight and hotel search)
    
    Raises:
        ValueError: If any required API key is missing
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Check for required API keys
    required_keys = ['OPENAI_API_KEY', 'TAVILY_API_KEY', 'SERPAPI_API_KEY']
    missing_keys = []
    
    for key in required_keys:
        if not os.environ.get(key):
            missing_keys.append(key)
    
    if missing_keys:
        raise ValueError(
            f"Missing required API keys: {', '.join(missing_keys)}\n"
            f"Please set them in your .env file or as environment variables."
        )
    
    print("✅ All API keys loaded successfully!")
    return True

def get_api_key(key_name: str) -> str:
    """
    Get a specific API key from environment variables.
    
    Args:
        key_name: Name of the API key (e.g., 'OPENAI_API_KEY')
    
    Returns:
        The API key value
        
    Raises:
        ValueError: If the key is not found
    """
    value = os.environ.get(key_name)
    if not value:
        raise ValueError(f"API key '{key_name}' not found in environment variables")
    return value
