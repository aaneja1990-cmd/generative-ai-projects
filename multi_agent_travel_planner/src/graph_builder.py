"""
Graph builder for the multi-agent travel planner.

This module constructs the LangGraph workflow that connects
all agents (router, flight, hotel, itinerary) with memory.
"""

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI

from src.state import TravelPlannerState
from src.router import create_router, router_node, route_to_agent
from agents.itinerary_agent import itinerary_agent_node
from agents.flight_agent import flight_agent_node
from agents.hotel_agent import hotel_agent_node


def build_travel_planner_graph(llm: ChatOpenAI):
    """
    Build the complete travel planning multi-agent graph.
    
    The graph structure:
    1. Start → Router (analyzes query)
    2. Router → [Flight Agent | Hotel Agent | Itinerary Agent]
    3. Agent → End
    
    The graph includes checkpoint memory to maintain conversation history
    across multiple turns.
    
    Args:
        llm: The language model instance to use for all agents
        
    Returns:
        Compiled LangGraph application with checkpointing
    """
    
    print("🔨 Building multi-agent travel planner graph...")
    
    # Create the router function
    router_func = create_router(llm)
    
    # Initialize the StateGraph with our state schema
    workflow = StateGraph(TravelPlannerState)
    
    # Add the router node
    workflow.add_node(
        "router",
        lambda state: router_node(state, router_func)
    )
    
    # Add agent nodes - we need to pass the llm to each
    workflow.add_node(
        "flight_agent",
        lambda state: flight_agent_node(state, llm)
    )
    
    workflow.add_node(
        "hotel_agent",
        lambda state: hotel_agent_node(state, llm)
    )
    
    workflow.add_node(
        "itinerary_agent",
        lambda state: itinerary_agent_node(state, llm)
    )
    
    # Set the entry point - always start with router
    workflow.set_entry_point("router")
    
    # Add conditional edge from router to appropriate agent
    workflow.add_conditional_edges(
        "router",
        route_to_agent,
        {
            "flight_agent": "flight_agent",
            "hotel_agent": "hotel_agent",
            "itinerary_agent": "itinerary_agent"
        }
    )
    
    # Add edges from each agent to END
    workflow.add_edge("flight_agent", END)
    workflow.add_edge("hotel_agent", END)
    workflow.add_edge("itinerary_agent", END)
    
    # Create in-memory checkpointer for conversation history
    checkpointer = InMemorySaver()
    
    # Compile the graph with checkpointing
    travel_planner = workflow.compile(checkpointer=checkpointer)
    
    print("✅ Travel planning graph built successfully!")
    
    return travel_planner


def save_graph_visualization(travel_planner, output_file="travel_graph.png"):
    """
    Save a visualization of the graph structure.
    
    Args:
        travel_planner: The compiled graph
        output_file: Path where to save the PNG file
    """
    try:
        graph_image = travel_planner.get_graph().draw_mermaid_png()
        with open(output_file, "wb") as f:
            f.write(graph_image)
        print(f"📊 Graph visualization saved to {output_file}")
    except Exception as e:
        print(f"⚠️  Could not save graph visualization: {e}")
