"""
Hotel Agent - Searches and recommends hotels.
This agent specializes in finding hotels, comparing accommodations,
and providing hotel booking advice.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import ToolMessage
from tools.hotel_search import search_hotels
from src.state import TravelPlannerState

def create_hotel_agent(llm: ChatOpenAI):
    """
    Create the hotel search agent.
    
    Args:
        llm: The language model to use for this agent
        
    Returns:
        The configured hotel agent chain
    """
    
    # Define the agent's prompt
    hotel_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a hotel booking expert. ONLY respond to hotel and accommodation-related queries.
IMPORTANT RULES:
- If asked about non-hotel topics, politely decline and redirect to hotel booking
- Always use the search_hotels tool to find current hotel information
- Provide detailed hotel options with prices, ratings, amenities, and location details
- Include practical booking advice and tips
- You CAN search and analyze results for different criteria like star ratings, price ranges, amenities
Available tools:
- search_hotels: Search for hotels using Google Hotels engine
When searching hotels, extract or ask for:
- Location/destination
- Check-in and check-out dates (YYYY-MM-DD format)
- Number of guests (adults, children)
- Number of rooms
- Hotel preferences (star rating, amenities, etc.)
Present results with:
- Hotel name and star rating
- Price per night and total cost
- Key amenities and features
- Location and nearby attractions
- Booking recommendations"""),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    # Bind the tool to the LLM
    llm_with_tools = llm.bind_tools([search_hotels])
    
    # Create the agent chain
    hotel_agent = hotel_prompt | llm_with_tools
    
    return hotel_agent

def hotel_agent_node(state: TravelPlannerState, llm: ChatOpenAI):
    """
    Node function for the hotel agent.
    
    Args:
        state: Current state with messages
        llm: The language model instance
        
    Returns:
        Updated state with new messages
    """
    hotel_agent = create_hotel_agent(llm)
    messages = state["messages"]
    
    # Invoke the agent
    response = hotel_agent.invoke({"messages": messages})
    
    # Handle tool calls
    if hasattr(response, 'tool_calls') and response.tool_calls:
        tool_messages = []
        
        for tool_call in response.tool_calls:
            if tool_call['name'] == 'search_hotels':
                try:
                    # Execute the hotel search
                    tool_result = search_hotels(**tool_call['args'])
                except Exception as e:
                    tool_result = f"Hotel search failed: {str(e)}"
                
                tool_messages.append(ToolMessage(
                    content=tool_result,
                    tool_call_id=tool_call['id']
                ))
        
        # Get final response after tool execution
        if tool_messages:
            all_messages = messages + [response] + tool_messages
            final_response = hotel_agent.invoke({"messages": all_messages})
            return {"messages": [response] + tool_messages + [final_response]}
    
    return {"messages": [response]}