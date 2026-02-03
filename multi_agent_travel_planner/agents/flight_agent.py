"""
Flight Agent - Searches and recommends flights.

This agent specializes in finding flights between airports,
comparing options, and providing flight booking advice.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import ToolMessage
from tools.flight_search import search_flights
from src.state import TravelPlannerState


def create_flight_agent(llm: ChatOpenAI):
    """
    Create the flight search agent.
    
    Args:
        llm: The language model to use for this agent
        
    Returns:
        The configured flight agent chain
    """
    
    # Define the agent's prompt
    flight_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a flight booking expert. ONLY respond to flight-related queries.

IMPORTANT RULES:
- If asked about non-flight topics, politely decline and redirect to flight booking
- Always use the search_flights tool to find current flight information
- You CAN search for flights and analyze the results for:
  * Direct flights vs connecting flights
  * Different airlines and flight classes
  * Various price ranges and timing options
  * Flight duration and layover information
- When users ask for specific preferences (direct flights, specific class, etc.), search first then filter/analyze the results
- Present results clearly organized by outbound and return flights

Available tools:
- search_flights: Search for comprehensive flight data that includes all airlines, classes, and connection types

Process:
1. ALWAYS search for flights first using the tool
2. Analyze the results to find flights matching user preferences
3. Present organized results with clear recommendations

Airport code mapping (common ones):
- Delhi: DEL
- Dubai: DXB
- London Heathrow: LHR
- New York: JFK/LGA/EWR
- Los Angeles: LAX
- Paris: CDG
- Tokyo: NRT/HND
- Singapore: SIN"""),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    # Bind the tool to the LLM
    llm_with_tools = llm.bind_tools([search_flights])
    
    # Create the agent chain
    flight_agent = flight_prompt | llm_with_tools
    
    return flight_agent


def flight_agent_node(state: TravelPlannerState, llm: ChatOpenAI):
    """
    Node function for the flight agent.
    
    Args:
        state: Current state with messages
        llm: The language model instance
        
    Returns:
        Updated state with new messages
    """
    flight_agent = create_flight_agent(llm)
    messages = state["messages"]
    
    # Invoke the agent
    response = flight_agent.invoke({"messages": messages})
    
    # Handle tool calls
    if hasattr(response, 'tool_calls') and response.tool_calls:
        tool_messages = []
        
        for tool_call in response.tool_calls:
            if tool_call['name'] == 'search_flights':
                try:
                    # Execute the flight search
                    tool_result = search_flights(**tool_call['args'])
                except Exception as e:
                    tool_result = f"Flight search failed: {str(e)}"
                
                tool_messages.append(ToolMessage(
                    content=tool_result,
                    tool_call_id=tool_call['id']
                ))
        
        # Get final response after tool execution
        if tool_messages:
            all_messages = messages + [response] + tool_messages
            final_response = flight_agent.invoke({"messages": all_messages})
            return {"messages": [response] + tool_messages + [final_response]}
    
    return {"messages": [response]}
