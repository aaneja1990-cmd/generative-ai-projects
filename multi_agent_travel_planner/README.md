# 🌍 Multi-Agent Travel Planner

A sophisticated travel planning system powered by multiple AI agents using LangGraph, LangChain, and GPT-4o. This system intelligently routes queries to specialized agents for flights, hotels, and itinerary planning.

## 🎯 Features

- **Intelligent Routing**: Automatically routes queries to the right specialist agent
- **Flight Search**: Real-time flight search using Google Flights via SERP API
- **Hotel Search**: Comprehensive hotel search with ratings, prices, and amenities
- **Itinerary Planning**: Detailed travel itineraries with web search capabilities
- **Conversational Memory**: Maintains context across multiple queries in a session
- **Interactive Chat**: Multi-turn conversations with the travel assistant

## 🏗️ Architecture

The system uses a multi-agent architecture built with LangGraph:

```
User Query → Router → [Flight Agent | Hotel Agent | Itinerary Agent] → Response
```

Each agent is a specialist:
- **Router**: Analyzes queries and routes to the appropriate agent
- **Flight Agent**: Searches and compares flights
- **Hotel Agent**: Finds and recommends hotels
- **Itinerary Agent**: Plans trips and provides travel advice

## 📁 Project Structure

```
multi_agent_travel_planner/
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Template for API keys
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── SETUP_GUIDE.md         # Detailed setup instructions
│
├── config/                # Configuration management
│   ├── __init__.py
│   └── settings.py        # Environment variable loading
│
├── src/                   # Core application logic
│   ├── __init__.py
│   ├── state.py          # State schema definition
│   ├── router.py         # Query routing logic
│   └── graph_builder.py  # LangGraph workflow builder
│
├── agents/               # Individual agent implementations
│   ├── __init__.py
│   ├── itinerary_agent.py  # Travel planning agent
│   ├── flight_agent.py     # Flight search agent
│   └── hotel_agent.py      # Hotel search agent
│
└── tools/                # External API tools
    ├── __init__.py
    ├── tavily_search.py   # Web search tool
    ├── flight_search.py   # Flight search via SERP API
    └── hotel_search.py    # Hotel search via SERP API
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for:
  - OpenAI (GPT-4o)
  - Tavily (web search)
  - SERP API (flight & hotel search)

### Installation

#### Option 1: Automated Setup (Recommended) ⚡

Run the setup script for your operating system:

**Windows:**
```bash
setup.bat
```

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

The script will:
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Validate your setup
- ✅ Guide you through API key configuration

#### Option 2: Manual Setup

1. **Clone or navigate to the project directory**:
   ```bash
   cd multi_agent_travel_planner
   ```

2. **Create a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys**:
   - Copy `.env.example` to `.env`
   - Add your API keys to `.env`
   ```bash
   cp .env.example .env
   # Edit .env with your favorite text editor
   ```

### Running the Application

**Interactive Chat Mode** (recommended for first-time users):
```bash
python main.py
```

**Single Query Mode**:
```bash
python main.py "Find flights from NYC to London on 2025-12-01"
```

## 💡 Usage Examples

### Flight Queries
```
"Find flights from New York to Dubai on 2025-11-30"
"Search for round-trip flights JFK to LHR December 1-10"
"Book me a flight to Paris for 2 people"
```

### Hotel Queries
```
"Find hotels in Tokyo for December 1-5"
"Show me 4-star hotels in Paris for 2 adults"
"Where should I stay in Bali?"
```

### Itinerary Queries
```
"Plan a 5-day trip to Italy"
"What are the best attractions in Rome?"
"Create an itinerary for Japan with kids"
"What's the weather like in Paris in December?"
```

## 🔑 Getting API Keys

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key to your `.env` file

### Tavily API Key
1. Visit [Tavily Dashboard](https://app.tavily.com/home)
2. Sign in or create an account
3. Go to the API Keys section
4. Copy your API key to your `.env` file

### SERP API Key
1. Visit [SERP API Dashboard](https://serpapi.com/dashboard)
2. Sign up or log in
3. Copy your private API key
4. Add it to your `.env` file

## 📚 Key Differences: Colab vs Local

### Google Colab
- ✅ No setup required
- ✅ Free GPU access
- ✅ Pre-installed packages
- ❌ Session-based (loses data on disconnect)
- ❌ Uses `userdata.get()` for secrets
- ❌ Requires `!pip install` commands

### Local VS Code
- ✅ Persistent storage
- ✅ Better debugging tools
- ✅ Full control over environment
- ✅ Uses `.env` file for secrets
- ❌ Requires manual setup
- ❌ Uses `pip install` (no `!`)

### Key Code Changes from Colab
1. **API Keys**: `userdata.get()` → `.env` file with `python-dotenv`
2. **Installation**: `!pip install` → `pip install`
3. **Structure**: Single notebook → Multiple Python files
4. **Imports**: All imports at file top, not scattered
5. **Virtual Environment**: Required for local development

## 🛠️ Troubleshooting

### "No module named 'langchain'"
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### "API key not found"
- Check that `.env` file exists in project root
- Verify all API keys are set in `.env`
- Ensure no extra spaces in `.env` file

### "Module not found" errors
```bash
# Run from the project root directory
cd /path/to/multi_agent_travel_planner
python main.py
```

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new agents (e.g., weather agent, restaurant agent)
- Improve error handling
- Add tests
- Enhance the UI

## 📖 Learn More

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

## 📝 License

This project is for educational purposes.

---

**Built with ❤️ using LangGraph, LangChain, and GPT-4o**
