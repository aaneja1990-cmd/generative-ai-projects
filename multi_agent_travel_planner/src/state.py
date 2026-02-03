"""
State schema for the multi-agent travel planner system.

This module defines the state structure that is passed between agents
in the LangGraph workflow.
"""

from typing import TypedDict, Annotated, List, Optional
import operator
from langchain_core.messages import BaseMessage


class TravelPlannerState(TypedDict):
    """
    State schema for the travel planning multi-agent system.
    
    This state is passed between agents and maintains the conversation
    history, routing information, and current query.
    
    Attributes:
        messages: List of conversation messages (user and AI messages)
                 The 'operator.add' annotation means new messages are appended
                 to the list rather than replacing it
        next_agent: The name of the next agent to route to
        user_query: The current user's query/question
    """
    
    # Conversation history - automatically appended with operator.add
    messages: Annotated[List[BaseMessage], operator.add]
    
    # Agent routing information
    next_agent: Optional[str]
    
    # Current user query
    user_query: Optional[str]
