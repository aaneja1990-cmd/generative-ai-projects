from agents.types import TravelState

def destination_agent(state: TravelState) -> TravelState:
    """ LangGraph node for destination agent """
    print("🔧 destination_agent running…")
    q = state.get("user_input", "").lower()

    if "beach" in q:
        dest = "Bali"
    elif "snow" in q or "mountain" in q:
        dest = "Manali"
    else:
        dest = "Kyoto"  # sensible default

    print(f"🌍 Suggested destination: {dest}")
    return {**state, "destination": dest}

def itinerary_agent(state: TravelState) -> TravelState:
    """ LangGraph node for itinerary agent """
    print("🔧 itinerary_agent running…")
    dest = state["destination"]
    plan = (
        f"Day 1: Arrive in {dest}\n"
        f"Day 2: Explore iconic spots in {dest}\n"
        f"Day 3: Relax + sample local cuisine"
    )
    print(f"🧳 Draft itinerary:\n{plan}")
    return {**state, "itinerary": plan}

def activity_agent(state: TravelState) -> TravelState:
    """ LangGraph node for activity agent """
    print("🔧 activity_agent running…")
    dest = state["destination"]
    act = (
        "Snorkelling • Beach yoga"
        if dest == "Bali"
        else "Skiing • Mountain trek"
    )
    print(f"🎯 Suggested activities: {act}")
    return {**state, "activities": act}