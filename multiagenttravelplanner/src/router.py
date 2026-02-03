"""
Router module for the multi-agent travel planner.
The router analyzes user queries and determines which specialist agent
should handle the request (flight, hotel, or itinerary).
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.state import TravelPlannerState


def create_router(llm: ChatOpenAI):
    """
    Create a router that decides which agent should handle a query.

    The router is an LLM-based classifier that analyzes the user's
    question and routes it to the appropriate specialist agent.

    Args:
        llm: The language model to use for routing decisions

    Returns:
        A function that takes state and returns the next agent name
    """

    # Define the router's prompt
    router_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a routing expert for a travel planning system.
Analyze the user's query and decide which specialist agent should handle it:
- FLIGHT: Flight bookings, airlines, air travel, flight search, tickets, airports, departures, arrivals, airline prices
- HOTEL: Hotels, accommodations, stays, rooms, hotel bookings, lodging, resorts, hotel search, hotel prices
- ITINERARY: Travel itineraries, trip planning, destinations, activities, attractions, sightseeing, travel advice, weather, culture, food, general travel questions
Respond with ONLY one word: FLIGHT, HOTEL, or ITINERARY
Examples:
"Book me a flight to Paris" → FLIGHT
"Find hotels in Tokyo" → HOTEL
"Plan my 5-day trip to Italy" → ITINERARY
"Search flights from NYC to London" → FLIGHT
"Where should I stay in Bali?" → HOTEL
"What are the best attractions in Rome?" → ITINERARY
"I need airline tickets" → FLIGHT
"Show me hotel options" → HOTEL
"Create an itinerary for Japan" → ITINERARY"""),
        ("user", "Query: {query}")
    ])

    # Create the router chain
    router_chain = router_prompt | llm | StrOutputParser()

    def route_query(state: TravelPlannerState):
        """
        Router function - decides which agent to call next.

        Args:
            state: Current state containing messages

        Returns:
            Name of the next agent to invoke
        """
        # Get the latest user message
        user_message = state["messages"][-1].content

        print(f"🧭 Router analyzing: '{user_message[:50]}...'")

        try:
            # Get LLM routing decision
            decision = router_chain.invoke({"query": user_message}).strip().upper()

            # Validate decision
            if decision not in ["FLIGHT", "HOTEL", "ITINERARY"]:
                print(f"⚠️  Invalid decision '{decision}', defaulting to ITINERARY")
                decision = "ITINERARY"

            # Map decision to agent node names
            agent_mapping = {
                "FLIGHT": "flight_agent",
                "HOTEL": "hotel_agent",
                "ITINERARY": "itinerary_agent"
            }

            next_agent = agent_mapping.get(decision, "itinerary_agent")
            print(f"🎯 Router decision: {decision} → {next_agent}")

            return next_agent

        except Exception as e:
            print(f"⚠️  Router error, defaulting to itinerary_agent: {e}")
            return "itinerary_agent"

    return route_query


def router_node(state: TravelPlannerState, router_func):
    """
    Router node for the LangGraph workflow.

    This is called as a node in the graph and updates the state
    with routing information.

    Args:
        state: Current state
        router_func: The routing function to use

    Returns:
        Updated state with next_agent and user_query
    """
    user_message = state["messages"][-1].content
    next_agent = router_func(state)

    return {
        "next_agent": next_agent,
        "user_query": user_message
    }


def route_to_agent(state: TravelPlannerState):
    """
    Conditional edge function for LangGraph.

    This determines which path to take after the router node.

    Args:
        state: Current state with next_agent set

    Returns:
        Name of the agent to route to
    """
    next_agent = state.get("next_agent")

    if next_agent == "flight_agent":
        return "flight_agent"
    elif next_agent == "hotel_agent":
        return "hotel_agent"
    elif next_agent == "itinerary_agent":
        return "itinerary_agent"
    else:
        # Default fallback
        return "itinerary_agent"