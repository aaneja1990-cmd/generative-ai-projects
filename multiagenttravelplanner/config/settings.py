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
    print(f"[INFO] Loaded API keys: " +
            f"OPENAI_API_KEY={'set' if os.environ.get('OPENAI_API_KEY') else 'not set'}, " +
            f"TAVILY_API_KEY={'set' if os.environ.get('TAVILY_API_KEY') else 'not set'}, " +
            f"SERPAPI_API_KEY={'set' if os.environ.get('SERPAPI_API_KEY') else 'not set'}")
    
    if missing_keys:
        raise ValueError(f"Missing required API keys: {', '.join(missing_keys)}\n"
                         f"Please ensure they are set in the .env file.")
    
    print("✅ All API keys loaded successfully!")
    return True

def get_api_key(key_name: str) -> str:
    """
    Retrieve the specified API key from environment variables.
    
    Args:
        key_name (str): The name of the API key to retrieve.
    Returns:
        str: The API key value.
    Raises:
        KeyError: If the specified API key is not found.
    """
    
    value = os.environ.get(key_name)
    if not value:
        raise KeyError(f"API key '{key_name}' not found in environment variables.")
    return value