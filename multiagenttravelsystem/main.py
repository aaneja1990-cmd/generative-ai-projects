"""
Main entry point for the Multi-Agent Travel Planning System

This is the orchestrator that coordinates all agents:
1. Takes user input (destination, dates, budget)
2. Calls itinerary agent to find attractions
3. Calls flight agent to find flights
4. Returns comprehensive travel plan
"""

import logging
import sys
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from multiagenttravelsystem.load_env import require_api_keys
from multiagenttravelsystem.agents.itinerary_agent import find_top_attractions
from multiagenttravelsystem.agents.flight_search_agent import search_flights
from multiagenttravelsystem.core.state import TravelState
from multiagenttravelsystem.utils.validators import (
    validate_destination,
    validate_trip_duration,
    sanitize_input
)


def create_travel_plan(destination: str, trip_duration: int = 5) -> dict:
    """
    Create a comprehensive travel plan for a destination
    
    Args:
        destination: Where the user wants to go
        trip_duration: How many days (default 5)
    
    Returns:
        Dictionary with itinerary and flights
    """
    logger.info(f"Creating travel plan for {destination} ({trip_duration} days)")
    
    # Validate inputs
    if not validate_destination(destination):
        raise ValueError(f"Invalid destination: {destination}")
    
    if not validate_trip_duration(trip_duration):
        raise ValueError(f"Invalid trip duration: {trip_duration}")
    
    # Sanitize input
    destination = sanitize_input(destination)
    
    try:
        # Step 1: Get attractions and itinerary
        logger.info(f"Step 1/2: Finding attractions in {destination}...")
        attractions = find_top_attractions(f"Best things to do in {destination}")
        
        # Step 2: Get flight options
        logger.info("Step 2/2: Searching for flights...")
        # Note: flight_search_agent needs from/to cities - using placeholder
        flights = search_flights(
            from_city="New York",  # Can be parameterized
            to_city=destination,
            days_until_departure=30
        )
        
        # Combine results
        travel_plan = {
            "destination": destination,
            "duration_days": trip_duration,
            "attractions": attractions,
            "flights": flights,
            "status": "success"
        }
        
        logger.info(f"Travel plan created successfully for {destination}")
        return travel_plan
        
    except Exception as e:
        logger.error(f"Error creating travel plan: {str(e)}")
        return {
            "destination": destination,
            "status": "error",
            "error": str(e)
        }


def display_travel_plan(plan: dict) -> None:
    """
    Pretty print the travel plan
    
    Args:
        plan: Travel plan dictionary
    """
    print("\n" + "="*60)
    print(f"✈️  TRAVEL PLAN FOR {plan.get('destination', 'Unknown').upper()}")
    print("="*60 + "\n")
    
    if plan.get("status") == "error":
        print(f"❌ Error: {plan.get('error')}")
        return
    
    print(f"📅 Duration: {plan.get('duration_days', 'N/A')} days\n")
    
    print("🏖️  TOP ATTRACTIONS:")
    print("-" * 60)
    attractions = plan.get("attractions", [])
    if attractions:
        for i, attraction in enumerate(attractions[:5], 1):
            print(f"{i}. {attraction}")
    else:
        print("No attractions found")
    
    print("\n✈️  AVAILABLE FLIGHTS:")
    print("-" * 60)
    flights = plan.get("flights", [])
    if flights:
        for i, flight in enumerate(flights[:3], 1):
            print(f"{i}. {flight}")
    else:
        print("No flights found")
    
    print("\n" + "="*60 + "\n")


def main():
    """Main function - orchestrates the entire flow"""
    
    print("\n" + "="*60)
    print("🌍 MULTI-AGENT TRAVEL PLANNING SYSTEM")
    print("="*60 + "\n")
    
    try:
        # Check that all API keys are available
        logger.info("Validating API keys...")
        require_api_keys()
        
        # Example usage - can be extended for user input
        destination = "Paris"
        duration = 5
        
        print(f"Planning trip to: {destination}")
        print(f"Duration: {duration} days\n")
        
        # Create travel plan
        plan = create_travel_plan(destination, duration)
        
        # Display results
        display_travel_plan(plan)
        
        logger.info("Travel planning completed successfully")
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        print(f"❌ Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        print(f"❌ Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
