"""
Hotel search tool using Google Hotels via SERP API.
This tool searches for hotels in a specified location with given dates.
"""

import os
import json
import serpapi
from dotenv import load_dotenv

# Ensure .env is loaded
load_dotenv()

def search_hotels(location: str, check_in_date: str, check_out_date: str, adults: int = 1, children: int = 0, rooms: int = 1, hotel_class: str = None, sort_by: int = 8) -> str:
    """
    Search for hotels using Google Hotels engine via SERP API.
    
    Args:
        location: Location to search for hotels (e.g., 'New York', 'Paris', 'Tokyo')
        check_in_date: Check-in date in YYYY-MM-DD format
        check_out_date: Check-out date in YYYY-MM-DD format
        adults: Number of adults (default: 1)
        children: Number of children (default: 0)
        rooms: Number of rooms needed (default: 1)
        hotel_class: Optional hotel star rating filter (e.g., '3,4,5' for 3-5 star hotels)
        sort_by: Sort order parameter (default: 8 for highest rating)
    
    Returns:
        JSON string containing hotel search results (top 5 properties)
        
    Example:
        >>> results = search_hotels('Paris', '2025-12-01', '2025-12-05', adults=2, hotel_class='4,5')
    """
    
    # Ensure proper integer types
    adults = int(float(adults)) if adults else 1
    children = int(float(children)) if children else 0
    rooms = int(float(rooms)) if rooms else 1
    sort_by = int(float(sort_by)) if sort_by else 8
    
    # Build search parameters
    params = {
        'api_key': os.environ.get('SERPAPI_API_KEY'),
        'engine': 'google_hotels',
        'hl': 'en',  # Language: English
        'gl': 'us',  # Country: US
        'q': location,  # Search query (location)
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'currency': 'USD',
        'adults': adults,
        'children': children,
        'rooms': rooms,
        'sort_by': sort_by
    }
    
    # Add hotel class filter if provided
    if hotel_class:
        params['hotel_class'] = hotel_class

    try:
        # Execute the search
        print(f"[DEBUG] Searching hotels: {location}, {check_in_date} to {check_out_date}")
        search = serpapi.search(params)
        
        # Check if we have data
        if not hasattr(search, 'data') or not search.data:
            return json.dumps({
                "error": "No data returned from SerpAPI",
                "params_used": {k: v for k, v in params.items() if k != 'api_key'}
            }, indent=2)
        
        # Get hotel results (top 5 properties)
        results = search.data.get('properties', [])
        
        if not results:
            return json.dumps({
                "error": "No hotels found",
                "available_keys": list(search.data.keys()),
                "params_used": {k: v for k, v in params.items() if k != 'api_key'}
            }, indent=2)
        
        # Return formatted JSON results
        print(f"[DEBUG] Found {len(results)} hotel options")
        return json.dumps(results[:5], indent=2)
        
    except Exception as e:
        return f"Hotel search failed: {str(e)}"