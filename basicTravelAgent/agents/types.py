from typing import TypedDict

class TravelState(TypedDict, total=False):
    user_input: str          # raw question
    destination: str         # “Bali”, “Manali”, …
    itinerary: str           # multi-day plan
    activities: str          # granular activities
