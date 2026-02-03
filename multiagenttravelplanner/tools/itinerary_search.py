"""
Itinerary Search uses Tavily web search tool for gathering travel information.
This tool uses Tavily's search API to find current information about
destinations, attractions, and travel-related topics.
"""

import os
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

# Ensure .env is loaded
load_dotenv()

def create_itinerary_tool():
    """
    Create and return a TavilySearch tool instance.
    
    Returns:
        TavilySearch: Configured Tavily search tool
        
    Note:
        Requires TAVILY_API_KEY to be set in environment variables
    """
    tool = TavilySearch(max_results=5)
    return tool