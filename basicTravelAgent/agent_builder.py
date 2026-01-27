from agents.travel_agent import destination_agent, itinerary_agent, activity_agent
from langgraph.graph import StateGraph
from IPython.display import Image, display
from agents.types import TravelState

# Build the travel agent graph
builder = StateGraph(TravelState)

builder.add_node("destination_agent", destination_agent)
builder.add_node("itinerary_agent", itinerary_agent)
builder.add_node("activity_agent", activity_agent)

builder.set_entry_point("destination_agent")
builder.add_edge("destination_agent", "itinerary_agent")
builder.add_edge("itinerary_agent", "activity_agent")
builder.set_finish_point("activity_agent")

# Compile the graph
travel_graph = builder.compile()
print("Travel agent graph built successfully.")

# Save the graph visualization as an image file
graph_image = travel_graph.get_graph().draw_mermaid_png()
with open("travel_graph.png", "wb") as f:
    f.write(graph_image)
print("Graph visualization saved as 'travel_graph.png'")

initial_state: TravelState = {
    "user_input": "I want a beach vacation with lots of fun activities."
}
final_state = travel_graph.invoke(initial_state)
print("\nFinal Travel State:")
for key, value in final_state.items():
    print(f"{key}: {value}")