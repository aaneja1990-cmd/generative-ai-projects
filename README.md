# generative-ai-projects

Applied Generative AI projects exploring LLMs, RAG, agents, evaluation, and orchestration across modern GenAI frameworks and tooling, including `langchain`, `langgraph`, CrewAI, and LangSmith.

**Contents**
- **Project:**: A collection of small example projects demonstrating agent orchestration with LangGraph and LangChain.
- **Simple Travel Agent:**: A minimal multi-node agent linear graph that suggests destinations, builds a short itinerary, and recommends activities.

**Key Files**
- **`basicTravelAgent/agent_builder.py`**: Builds and runs the LangGraph `StateGraph` for the travel agent. Compiles the graph, saves a visualization as `travel_graph.png`, and invokes the graph with a sample input.
- **`basicTravelAgent/agents/travel_agent.py`**: Node implementations (`destination_agent`, `itinerary_agent`, `activity_agent`) and simple business logic used by the graph.
- **`basicTravelAgent/agents/types.py`**: Shared `TravelState` TypedDict used across modules (keeps type definitions in one place).
- **`run_basic_travel_agent.sh`**: Convenience script (project root) that sets `PYTHONPATH` and runs `agent_builder.py` using the workspace virtual environment.
- **`travel_graph.png`**: Example PNG produced by the graph visualization.

**Python environment**
- **Virtualenv**: The project uses a workspace virtual environment at `.venv` (configured by the editor tooling). Use the venv Python when running scripts.
- **Notable packages**: `langgraph`, `langchain`, `ipython` (for `IPython.display`), and their dependencies.

**Quick start (run the travel agent)**
1. From the project root, make the runner executable (if needed) and run:

```bash
chmod +x ./run_basic_travel_agent.sh
./run_basic_travel_agent.sh
```

2. Output: the script prints node logs, saves `travel_graph.png` in the project root, and prints the final `TravelState`.