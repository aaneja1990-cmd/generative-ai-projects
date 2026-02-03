"""
Main entry point for the Multi-Agent Travel Planner.

This script provides both interactive chat mode and single-query mode
for the travel planning system.
"""

import sys
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Import our modules
from config.settings import load_config
from src.graph_builder import build_travel_planner_graph, save_graph_visualization


def initialize_system():
    """
    Initialize the travel planner system.
    
    This loads configuration, creates the LLM, and builds the graph.
    
    Returns:
        tuple: (travel_planner_graph, llm)
    """
    print("=" * 60)
    print("🚀 Initializing Multi-Agent Travel Planner")
    print("=" * 60)
    
    # Load API keys from .env file
    try:
        load_config()
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nPlease ensure you have:")
        print("1. Created a .env file in the project root")
        print("2. Added all required API keys (see .env.example)")
        sys.exit(1)
    
    # Initialize the language model
    print("\n🤖 Initializing GPT-4o...")
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.2
    )
    
    # Build the multi-agent graph
    travel_planner = build_travel_planner_graph(llm)
    
    # Save graph visualization
    save_graph_visualization(travel_planner, "travel_graph.png")
    
    return travel_planner, llm


def run_single_query(travel_planner, query, thread_id="default"):
    """
    Run a single query through the system.
    
    Args:
        travel_planner: The compiled graph
        query: User's question/request
        thread_id: Session identifier for memory
    """
    print(f"\n{'=' * 60}")
    print(f"🧑 User: {query}")
    print(f"{'=' * 60}")
    
    # Create initial state with the user's message
    initial_state = {
        "messages": [HumanMessage(content=query)],
        "next_agent": ""
    }
    
    # Configuration for checkpointing (memory)
    config = {"configurable": {"thread_id": thread_id}}
    
    # Run the system
    result = travel_planner.invoke(initial_state, config)
    
    # Get and display the response
    response = result["messages"][-1].content
    print(f"\n🤖 Assistant:\n{response}")
    print(f"\n{'-' * 60}\n")


def run_interactive_chat(travel_planner):
    """
    Run an interactive multi-turn conversation.
    
    This maintains conversation history across multiple queries
    within the same session.
    
    Args:
        travel_planner: The compiled graph
    """
    print("\n" + "=" * 60)
    print("💬 Multi-Agent Travel Assistant (Interactive Mode)")
    print("=" * 60)
    print("\nHow to use:")
    print("- Ask about flights: 'Find flights from NYC to London'")
    print("- Ask about hotels: 'Find hotels in Paris'")
    print("- Ask about itineraries: 'Plan a 5-day trip to Japan'")
    print("- Type 'quit' to exit")
    print("=" * 60)
    
    # Use a consistent thread ID for the session
    config = {"configurable": {"thread_id": "interactive_session"}}
    
    while True:
        # Get user input
        user_input = input("\n🧑 You: ").strip()
        
        # Check for exit
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Thank you for using the Multi-Agent Travel Planner!")
            break
        
        if not user_input:
            continue
        
        print(f"\n📊 Processing your query...")
        
        try:
            # Invoke the graph with the new message
            result = travel_planner.invoke(
                {"messages": [HumanMessage(content=user_input)]},
                config
            )
            
            # Display the response
            response = result["messages"][-1].content
            print(f"\n🤖 Assistant:\n{response}")
            print(f"\n{'-' * 60}")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again with a different query.")


def main():
    """
    Main function - entry point of the application.
    """
    # Initialize the system
    travel_planner, llm = initialize_system()
    
    # Check if user provided a query as command line argument
    if len(sys.argv) > 1:
        # Single query mode
        query = " ".join(sys.argv[1:])
        run_single_query(travel_planner, query)
    else:
        # Interactive chat mode
        run_interactive_chat(travel_planner)


if __name__ == "__main__":
    main()
