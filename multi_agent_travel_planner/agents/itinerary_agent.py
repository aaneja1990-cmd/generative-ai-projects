"""
Itinerary Agent - Plans travel itineraries and provides travel advice.

This agent specializes in creating detailed travel itineraries,
suggesting destinations, and answering general travel questions.
"""

import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import ToolMessage
from tools.tavily_search import create_tavily_tool
from src.state import TravelPlannerState


def create_itinerary_agent(llm: ChatOpenAI):
    """
    Create the itinerary planning agent.
    
    Args:
        llm: The language model to use for this agent
        
    Returns:
        The configured itinerary agent chain
    """
    
    # Create the Tavily search tool
    tool = create_tavily_tool()
    
    # Define the agent's prompt with system instructions
    itinerary_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert travel itinerary planner. ONLY respond to travel planning and itinerary-related questions.

IMPORTANT RULES:
- If asked about non-travel topics (weather, math, general questions), politely decline and redirect to travel planning
- Always provide complete, well-formatted itineraries with specific details
- Include timing, locations, transportation, and practical tips

Use the ReAct approach:
1. THOUGHT: Analyze what travel information is needed
2. ACTION: Search for current information about destinations, attractions, prices, hours
3. OBSERVATION: Process the search results
4. Provide a comprehensive, formatted response

Available tools:
- TavilySearch: Search for current travel information

Format your itineraries with:
- Clear day-by-day breakdown
- Specific times and locations
- Transportation between locations
- Estimated costs when possible
- Practical tips and recommendations"""),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    # Bind the tool to the LLM
    llm_with_tools = llm.bind_tools([tool])
    
    # Create the agent chain
    itinerary_agent = itinerary_prompt | llm_with_tools
    
    return itinerary_agent, tool


def itinerary_agent_node(state: TravelPlannerState, llm: ChatOpenAI):
    """
    Node function for the itinerary agent.
    
    This function is called by LangGraph when routing to the itinerary agent.
    It processes messages, handles tool calls, and returns updated state.
    
    Args:
        state: Current state with messages and other info
        llm: The language model instance
        
    Returns:
        Updated state with new messages
    """
    # Get the agent and tool
    itinerary_agent, tool = create_itinerary_agent(llm)
    
    messages = state["messages"]
    
    # Invoke the agent with current messages
    response = itinerary_agent.invoke({"messages": messages})
    
    # Check if the agent wants to use tools
    if hasattr(response, 'tool_calls') and response.tool_calls:
        tool_messages = []
        
        # Execute each tool call
        for tool_call in response.tool_calls:
            if tool_call['name'] == 'tavily_search_results_json':
                try:
                    # Execute the search
                    tool_result = tool.search(
                        query=tool_call['args']['query'],
                        max_results=2
                    )
                    tool_result = json.dumps(tool_result, indent=2)
                except Exception as e:
                    tool_result = f"Search failed: {str(e)}"
                
                # Create a tool message with the result
                tool_messages.append(ToolMessage(
                    content=tool_result,
                    tool_call_id=tool_call['id']
                ))
        
        # If we have tool results, invoke the agent again with them
        if tool_messages:
            all_messages = messages + [response] + tool_messages
            final_response = itinerary_agent.invoke({"messages": all_messages})
            return {"messages": [response] + tool_messages + [final_response]}
    
    # No tool calls, just return the response
    return {"messages": [response]}
