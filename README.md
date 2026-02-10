# 🚀 Generative AI Projects

Applied Generative AI projects exploring LLMs, RAG, agents, evaluation, and orchestration across modern GenAI frameworks and tooling, including `langchain`, `langgraph`, CrewAI, and LangSmith.

---

## 📂 Projects

### 1️⃣ Basic Travel Agent (`basicTravelAgent/`)

A minimal multi-node agent linear graph that suggests destinations, builds a short itinerary, and recommends activities.

**Architecture:** Simple linear workflow (Destination → Itinerary → Activity)

**Key Files:**
- `agent_builder.py`: Builds and runs the LangGraph `StateGraph`
- `agents/travel_agent.py`: Node implementations (`destination_agent`, `itinerary_agent`, `activity_agent`)
- `agents/types.py`: Shared `TravelState` TypedDict

**Quick Start:**
```bash
chmod +x ./run_basic_travel_agent.sh
./run_basic_travel_agent.sh
```

**Output:** Prints node logs, saves `travel_graph.png`, and displays final `TravelState`

---

### 2️⃣ Multi-Agent Travel Planner (`multi_agent_travel_planner/`) ⭐ NEW!

A sophisticated multi-agent system with intelligent routing, real-time API integrations, and conversational memory.

**Architecture:** Router-based multi-agent system with specialized agents

**Features:**
- 🧭 **Intelligent Router**: Automatically routes queries to the right specialist
- ✈️ **Flight Agent**: Real-time flight search via Google Flights
- 🏨 **Hotel Agent**: Hotel search with ratings and prices
- 🗺️ **Itinerary Agent**: Detailed travel planning with web search
- 💬 **Conversational Memory**: Multi-turn conversations with context
- 🔧 **Production-Ready**: Organized code structure, comprehensive docs

**Tech Stack:**
- LangGraph for multi-agent orchestration
- LangChain for LLM framework
- GPT-4o for natural language understanding
- Tavily for web search
- SERP API for flights and hotels
- In-memory checkpointing for conversation history

**Quick Start:**
```bash
cd multi_agent_travel_planner
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add your API keys to .env
python main.py
```

**Documentation:**
- 📖 **README.md** - Project overview and quick start
- 📚 **SETUP_GUIDE.md** - Detailed step-by-step setup for beginners
- 🎓 **TUTORIAL.md** - Understanding multi-agent systems
- ⚡ **QUICK_REFERENCE.md** - Command cheat sheet

**Example Queries:**
```
"Find flights from NYC to London on December 1st"
"Find hotels in Paris for 3 nights"
"Plan a 5-day trip to Tokyo"
"What are the best attractions in Rome?"
```

---

## 🆚 Project Comparison

| Feature | Basic Travel Agent | Multi-Agent Travel Planner |
|---------|-------------------|---------------------------|
| **Architecture** | Linear workflow | Router-based multi-agent |
| **Agents** | 3 sequential | 4 with intelligent routing |
| **External APIs** | None | 3 (Tavily, SERP API) |
| **Memory** | None | Conversational checkpointing |
| **Interactivity** | Single run | Interactive chat |
| **Real-time Data** | ❌ | ✅ Flights, Hotels, Web |
| **Complexity** | Beginner | Intermediate |
| **Best For** | Learning basics | Production use cases |

---

## 🛠️ Development Environment

### Recommended Setup
- **Python**: 3.8 or higher
- **IDE**: VS Code with Python extension
- **Virtual Environment**: Use `venv` for each project

### Common Dependencies
```bash
# Both projects use:
langchain
langgraph
langchain-openai
ipython

# Multi-Agent Planner additionally uses:
tavily-python
serpapi
python-dotenv
```

---

## 📖 Learning Path

### Beginner
1. **Start with Basic Travel Agent** (`basicTravelAgent/`)
   - Understand LangGraph basics
   - Learn about state management
   - See simple agent workflows

2. **Read the code** in `basicTravelAgent/agents/travel_agent.py`
   - Understand node functions
   - See how state flows

### Intermediate
3. **Explore Multi-Agent Travel Planner** (`multi_agent_travel_planner/`)
   - **Quick Setup**: Run `setup.sh` (Linux/Mac) or `setup.bat` (Windows) for automated installation
   - Read `TUTORIAL.md` for concepts
   - Follow `SETUP_GUIDE.md` for manual setup
   - Run the interactive chat

4. **Understand the architecture**
   - Study the router logic
   - See how agents use tools
   - Learn about memory/checkpointing

### Advanced
5. **Extend the system**
   - Add a new agent (weather, restaurants)
   - Create custom tools
   - Modify routing logic
   - Implement advanced features

---

## 🔑 API Keys (Multi-Agent Planner Only)

The Multi-Agent Travel Planner requires three API keys:

| Service | Purpose | Get Key From | Free Tier |
|---------|---------|--------------|-----------|
| **OpenAI** | GPT-4o LLM | [platform.openai.com](https://platform.openai.com/api-keys) | Pay-as-you-go |
| **Tavily** | Web search | [app.tavily.com](https://app.tavily.com/home) | 1,000/month |
| **SERP API** | Flight/Hotel search | [serpapi.com](https://serpapi.com/dashboard) | 100/month |

Store in `.env` file (see `.env.example` in project directory)

---

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

## 🤝 Contributing

These are learning projects! Feel free to:
- Experiment with the code
- Add new features
- Create new agents
- Improve documentation
- Share your learnings

---

## 📝 License

Educational and personal use.

---

**Built with ❤️ using LangGraph, LangChain, and GPT-4o**