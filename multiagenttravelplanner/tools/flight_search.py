"""
Flight search tool using Google Flights via SERP API.
This tool searches for flights between airports on specified dates.
"""

import os
import json
import serpapi
from dotenv import load_dotenv

# Ensure .env is loaded
load_dotenv()

def search_flights(departure_airport: str, arrival_airport: str, outbound_date: str, return_date: str = None, adults: int = 1, children: int = 0) -> str:
    """
    Search for flights using Google Flights engine via SERP API.
    
    Args:
        departure_airport: Departure airport code (e.g., 'NYC', 'LAX', 'DEL')
        arrival_airport: Arrival airport code (e.g., 'LON', 'NRT', 'DXB')
        outbound_date: Departure date in YYYY-MM-DD format (e.g., '2025-11-30')
        return_date: Optional return date in YYYY-MM-DD format (for round trips)
        adults: Number of adult passengers (default: 1)
        children: Number of child passengers (default: 0)
    
    Returns:
        JSON string containing flight search results
        
    Example:
        >>> results = search_flights('JFK', 'LHR', '2025-12-01', '2025-12-10', adults=2)
    """
    # Ensure proper integer types (in case they're passed as strings)
    adults = int(float(adults)) if adults else 1
    children = int(float(children)) if children else 0
    
    # Build search parameters
    params = {
        'api_key': os.environ.get('SERPAPI_API_KEY'),
        'engine': 'google_flights',
        'hl': 'en',  # Language: English
        'gl': 'us',  # Country: US
        'departure_id': departure_airport,
        'arrival_id': arrival_airport,
        'outbound_date': outbound_date,
        'currency': 'USD',
        'adults': adults,
        'children': children,
        'type': '2' if not return_date else '1'  # 2=one-way, 1=round-trip
    }
    
    # Add return date if provided (for round trips)
    if return_date:
        params['return_date'] = return_date
        
    try:
        # Execute the search
        print(f"[DEBUG] Searching flights: {departure_airport} → {arrival_airport}, {outbound_date}")
        search = serpapi.search(params)
        
        # Check if we have data
        if not hasattr(search, 'data') or not search.data:
            return json.dumps({
                "error": "No data returned from SerpAPI",
                "params_used": {k: v for k, v in params.items() if k != 'api_key'}
            }, indent=2)
        
        # Try to get best flights first
        results = search.data.get('best_flights', [])
        
        # If no best flights, try other flights
        if not results:
            results = search.data.get('other_flights', [])
        
        # If still no results, return what we got
        if not results:
            return json.dumps({
                "error": "No flights found",
                "available_keys": list(search.data.keys()),
                "params_used": {k: v for k, v in params.items() if k != 'api_key'}
            }, indent=2)
        
        # Return formatted JSON results
        print(f"[DEBUG] Found {len(results)} flight options")
        return json.dumps(results[:5], indent=2)  # Limit to top 5
        
    except Exception as e:
        return json.dumps({
            "error": f"Flight search failed: {str(e)}",
            "params_used": {k: v for k, v in params.items() if k != 'api_key'}
        }, indent=2)