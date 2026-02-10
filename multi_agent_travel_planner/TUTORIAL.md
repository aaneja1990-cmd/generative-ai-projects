# 🎓 Understanding Multi-Agent Systems - A Complete Tutorial

This tutorial explains how the Multi-Agent Travel Planner works under the hood. Perfect for beginners who want to understand the concepts.

---

## 📚 Table of Contents

1. [What is a Multi-Agent System?](#what-is-a-multi-agent-system)
2. [Core Concepts](#core-concepts)
3. [How Our System Works](#how-our-system-works)
4. [Code Walkthrough](#code-walkthrough)
5. [Extending the System](#extending-the-system)

---

## 1. What is a Multi-Agent System?

### The Restaurant Analogy

Imagine you walk into a restaurant:

1. **Host (Router)**: Greets you and decides where to seat you
2. **Waiter (Flight Agent)**: Takes your food order
3. **Sommelier (Hotel Agent)**: Helps with wine selection
4. **Chef (Itinerary Agent)**: Prepares everything else

Each person has a **specific role** and **specialized knowledge**. They work together to serve you.

Our travel planner works the same way:

```
You: "I need a flight to Paris"
       ↓
Router: "This is a flight question, send to Flight Agent"
       ↓
Flight Agent: Uses flight search tool, returns results
       ↓
You: Get flight options
```

### Why Multi-Agent?

**Single Agent (Old Way):**
- One AI tries to do everything
- Gets confused with complex tasks
- Hard to update or fix specific features

**Multi-Agent (Our Way):**
- Each agent is an expert in one area
- Can add/remove agents easily
- Easier to debug and improve
- More reliable results

---

## 2. Core Concepts

### Concept 1: State

**What is it?**
State is like a **messenger envelope** that gets passed between agents.

**In our code:**
```python
class TravelPlannerState(TypedDict):
    messages: List[BaseMessage]      # Conversation history
    next_agent: Optional[str]        # Which agent to call next
    user_query: Optional[str]        # Current question
```

**Real-world example:**
```
State = {
    messages: [
        "User: Find flights to Paris",
        "Assistant: I'll search for flights..."
    ],
    next_agent: "flight_agent",
    user_query: "Find flights to Paris"
}
```

The state travels through the system, accumulating information.

### Concept 2: Agents

**What is it?**
An agent is a specialized AI with:
- **System Prompt**: Instructions on how to behave
- **Tools**: Functions it can use (search, calculate, etc.)
- **Logic**: How to process queries

**Our three agents:**

1. **Itinerary Agent**
   - Expert: Travel planning, destinations, activities
   - Tool: Web search (Tavily)
   - Role: Plans trips, answers general travel questions

2. **Flight Agent**
   - Expert: Flights, airlines, airports
   - Tool: Google Flights search (SERP API)
   - Role: Finds and compares flights

3. **Hotel Agent**
   - Expert: Hotels, accommodations
   - Tool: Google Hotels search (SERP API)
   - Role: Finds and recommends hotels

### Concept 3: Router

**What is it?**
The router is the "traffic cop" that decides which agent handles a query.

**How it works:**
1. Receives user query
2. Analyzes the content
3. Classifies it (FLIGHT, HOTEL, or ITINERARY)
4. Routes to appropriate agent

**Example:**
```python
Query: "Find hotels in Tokyo"
       ↓
Router thinks: "This mentions 'hotels', so route to HOTEL"
       ↓
Routes to: hotel_agent
```

### Concept 4: Tools

**What is it?**
Tools are **functions** that agents can call to get information.

**Example: Flight Search Tool**
```python
def search_flights(departure, arrival, date):
    # Calls Google Flights API
    # Returns flight data
    return flight_results
```

**When an agent uses a tool:**
1. Agent realizes it needs information
2. Calls the tool: `search_flights('JFK', 'LHR', '2025-12-01')`
3. Tool executes and returns data
4. Agent processes the data
5. Agent formulates a response

### Concept 5: Graph

**What is it?**
A graph is a visual representation of the workflow.

**Our graph:**
```
┌─────────┐
│  START  │
└────┬────┘
     │
     ▼
┌─────────┐
│ ROUTER  │  (Decides: Flight? Hotel? Itinerary?)
└────┬────┘
     │
     ├─────────────┬─────────────┐
     ▼             ▼             ▼
┌─────────┐  ┌─────────┐  ┌────────────┐
│ FLIGHT  │  │  HOTEL  │  │ ITINERARY  │
│  AGENT  │  │  AGENT  │  │   AGENT    │
└────┬────┘  └────┬────┘  └─────┬──────┘
     │            │              │
     └────────────┴──────────────┘
                  │
                  ▼
             ┌────────┐
             │  END   │
             └────────┘
```

---

## 3. How Our System Works

### Complete Flow Example

**User Query:** "Find flights from New York to London on December 1st"

#### Step 1: Initialization
```python
# main.py starts the system
llm = ChatOpenAI(model="gpt-4o")
travel_planner = build_travel_planner_graph(llm)
```

#### Step 2: User Message Arrives
```python
state = {
    "messages": [HumanMessage(content="Find flights...")],
    "next_agent": ""
}
```

#### Step 3: Router Node
```python
# src/router.py
def router_node(state):
    query = "Find flights from New York to London"
    
    # LLM analyzes query
    decision = llm.analyze(query)  # Returns "FLIGHT"
    
    return {
        "next_agent": "flight_agent"
    }
```

#### Step 4: Conditional Routing
```python
# Graph checks next_agent
if state["next_agent"] == "flight_agent":
    go_to_flight_agent()
```

#### Step 5: Flight Agent Processes
```python
# agents/flight_agent.py
def flight_agent_node(state):
    # Agent sees the query
    messages = state["messages"]
    
    # Agent decides to use flight search tool
    response = agent.invoke(messages)
    
    # Response includes a tool call:
    # tool_call = {
    #     'name': 'search_flights',
    #     'args': {
    #         'departure_airport': 'JFK',
    #         'arrival_airport': 'LHR',
    #         'outbound_date': '2025-12-01'
    #     }
    # }
```

#### Step 6: Tool Execution
```python
# tools/flight_search.py
results = search_flights(
    departure_airport='JFK',
    arrival_airport='LHR',
    outbound_date='2025-12-01'
)
# Returns: JSON with flight options
```

#### Step 7: Agent Processes Results
```python
# Agent gets tool results
tool_message = ToolMessage(content=results)

# Agent invokes LLM again with results
final_response = agent.invoke([
    original_query,
    tool_call_message,
    tool_results_message
])

# LLM formats the results nicely
return {
    "messages": [final_response]
}
```

#### Step 8: End
```python
# Graph reaches END node
# Final state is returned to user
result = travel_planner.invoke(state)
response = result["messages"][-1].content
print(response)
```

### Memory & Multi-Turn Conversations

**How memory works:**

```python
# First query
config = {"configurable": {"thread_id": "session_123"}}
result1 = travel_planner.invoke(state1, config)

# Second query (same session)
result2 = travel_planner.invoke(state2, config)
# System remembers previous messages!
```

**Behind the scenes:**
1. `InMemorySaver` stores conversation history
2. Each thread_id has its own memory
3. Messages accumulate in the state
4. Agents see full conversation context

---

## 4. Code Walkthrough

### main.py - Entry Point

```python
def main():
    # 1. Load configuration
    load_config()  # Loads API keys from .env
    
    # 2. Create LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
    
    # 3. Build graph
    travel_planner = build_travel_planner_graph(llm)
    
    # 4. Run interactive chat
    run_interactive_chat(travel_planner)
```

**What happens here:**
- Environment setup
- LLM initialization (connects to OpenAI)
- Graph construction (wires all agents together)
- User interface

### src/graph_builder.py - Building the Graph

```python
def build_travel_planner_graph(llm):
    workflow = StateGraph(TravelPlannerState)
    
    # Add nodes (agents)
    workflow.add_node("router", router_node)
    workflow.add_node("flight_agent", flight_agent_node)
    workflow.add_node("hotel_agent", hotel_agent_node)
    workflow.add_node("itinerary_agent", itinerary_agent_node)
    
    # Set starting point
    workflow.set_entry_point("router")
    
    # Add conditional routing
    workflow.add_conditional_edges(
        "router",           # From router
        route_to_agent,     # Decision function
        {                   # Possible destinations
            "flight_agent": "flight_agent",
            "hotel_agent": "hotel_agent",
            "itinerary_agent": "itinerary_agent"
        }
    )
    
    # All agents go to END
    workflow.add_edge("flight_agent", END)
    workflow.add_edge("hotel_agent", END)
    workflow.add_edge("itinerary_agent", END)
    
    # Add memory
    checkpointer = InMemorySaver()
    
    # Compile and return
    return workflow.compile(checkpointer=checkpointer)
```

**Key concepts:**
- `StateGraph`: Container for the workflow
- `add_node`: Adds an agent/processor
- `add_edge`: Connects nodes (A → B)
- `add_conditional_edges`: Routes based on logic
- `checkpointer`: Enables memory

### agents/flight_agent.py - An Agent

```python
def create_flight_agent(llm):
    # Define behavior with a prompt
    flight_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a flight expert. Only handle flight queries..."),
        MessagesPlaceholder(variable_name="messages")
    ])
    
    # Bind tools to LLM
    llm_with_tools = llm.bind_tools([search_flights])
    
    # Create chain: prompt → LLM with tools
    return flight_prompt | llm_with_tools

def flight_agent_node(state, llm):
    agent = create_flight_agent(llm)
    messages = state["messages"]
    
    # Invoke agent
    response = agent.invoke({"messages": messages})
    
    # Check if agent wants to use tools
    if response.tool_calls:
        # Execute tools
        # Get final response
        pass
    
    return {"messages": [response]}
```

**Key concepts:**
- `ChatPromptTemplate`: Defines agent's instructions
- `MessagesPlaceholder`: Where conversation history goes
- `bind_tools`: Gives agent access to functions
- Tool calling: Agent decides when to use tools

### tools/flight_search.py - A Tool

```python
def search_flights(departure_airport, arrival_airport, outbound_date):
    """Search for flights"""
    
    # Build API request
    params = {
        'api_key': os.environ.get('SERPAPI_API_KEY'),
        'engine': 'google_flights',
        'departure_id': departure_airport,
        'arrival_id': arrival_airport,
        'outbound_date': outbound_date
    }
    
    # Call external API
    search = serpapi.search(params)
    results = search.data.get('best_flights', [])
    
    # Return as JSON
    return json.dumps(results)
```

**Key concepts:**
- Simple Python function
- Takes parameters (from agent)
- Calls external API
- Returns data (to agent)

---

## 5. Extending the System

### Adding a New Agent

Let's add a **Weather Agent**!

#### Step 1: Create the Agent File

Create `agents/weather_agent.py`:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from src.state import TravelPlannerState

def create_weather_agent(llm):
    weather_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a weather expert. 
        ONLY respond to weather-related queries.
        Provide current weather and forecasts for travel destinations."""),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    return weather_prompt | llm

def weather_agent_node(state, llm):
    agent = create_weather_agent(llm)
    response = agent.invoke({"messages": state["messages"]})
    return {"messages": [response]}
```

#### Step 2: Update the Router

Edit `src/router.py`:

```python
router_prompt = ChatPromptTemplate.from_messages([
    ("system", """...
    
    - FLIGHT: Flight bookings...
    - HOTEL: Hotels...
    - ITINERARY: Travel itineraries...
    - WEATHER: Weather conditions, forecasts, climate  # ADD THIS
    
    Respond with: FLIGHT, HOTEL, ITINERARY, or WEATHER  # UPDATE THIS
    """),
    ...
])
```

#### Step 3: Update the Graph

Edit `src/graph_builder.py`:

```python
from agents.weather_agent import weather_agent_node  # Import

def build_travel_planner_graph(llm):
    workflow = StateGraph(TravelPlannerState)
    
    # Add nodes
    workflow.add_node("router", router_node)
    workflow.add_node("flight_agent", flight_agent_node)
    workflow.add_node("hotel_agent", hotel_agent_node)
    workflow.add_node("itinerary_agent", itinerary_agent_node)
    workflow.add_node("weather_agent", weather_agent_node)  # ADD THIS
    
    # ... (entry point setup)
    
    # Update conditional edges
    workflow.add_conditional_edges(
        "router",
        route_to_agent,
        {
            "flight_agent": "flight_agent",
            "hotel_agent": "hotel_agent",
            "itinerary_agent": "itinerary_agent",
            "weather_agent": "weather_agent"  # ADD THIS
        }
    )
    
    # Add edge to END
    workflow.add_edge("weather_agent", END)  # ADD THIS
    
    # ... (rest of code)
```

#### Step 4: Test It!

```bash
python main.py

You: What's the weather in Paris?
# Should route to weather_agent!
```

### Adding a New Tool

Let's add a **restaurant search tool**!

Create `tools/restaurant_search.py`:

```python
def search_restaurants(location, cuisine=None):
    """Search for restaurants"""
    # Your implementation here
    # Could use Yelp API, Google Places, etc.
    pass
```

Then bind it to an agent:

```python
# In itinerary_agent.py
from tools.restaurant_search import search_restaurants

llm_with_tools = llm.bind_tools([
    tavily_tool,
    search_restaurants  # Add your new tool
])
```

---

## 🎓 Key Takeaways

1. **Multi-Agent = Divide and Conquer**
   - Break complex tasks into specialized agents
   - Each agent has specific expertise

2. **State = Shared Memory**
   - Passes information between agents
   - Accumulates conversation history

3. **Router = Traffic Director**
   - Analyzes queries
   - Routes to correct agent

4. **Tools = External Actions**
   - Agents call tools to get real data
   - Tools can be any Python function

5. **Graph = Workflow Structure**
   - Defines how agents connect
   - Controls the flow of execution

6. **Memory = Conversation Context**
   - Checkpointer saves history
   - Enables multi-turn conversations

---

## 🚀 Next Steps

1. **Read the code**: Start with `main.py`, follow the imports
2. **Modify prompts**: Change agent behavior in agent files
3. **Add features**: Try adding a new agent or tool
4. **Experiment**: Break things, learn how they work!

---

**Happy Learning! 📚**

*The best way to understand is to experiment. Try changing things and see what happens!*
