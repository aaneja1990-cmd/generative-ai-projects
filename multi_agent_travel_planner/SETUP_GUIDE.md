# 📚 Complete Setup Guide for Beginners

This guide will walk you through setting up and running the Multi-Agent Travel Planner on your local machine. We'll explain every step in detail, assuming you have zero knowledge of Python development.

## 📋 Table of Contents

1. [What You'll Need](#what-youll-need)
2. [Understanding the Project Structure](#understanding-the-project-structure)
3. [Step-by-Step Setup](#step-by-step-setup)
4. [Getting API Keys](#getting-api-keys)
5. [Running the Application](#running-the-application)
6. [Understanding the Code](#understanding-the-code)
7. [Colab vs Local Development](#colab-vs-local-development)
8. [Troubleshooting](#troubleshooting)

---

## 1. What You'll Need

### Required Software

1. **Python 3.8 or higher**
   - Check if you have it: Open terminal/command prompt and type:
     ```bash
     python --version
     # or
     python3 --version
     ```
   - If not installed, download from [python.org](https://www.python.org/downloads/)
   - ⚠️ **Windows users**: Check "Add Python to PATH" during installation

2. **A Text Editor or IDE**
   - Recommended: [VS Code](https://code.visualstudio.com/) (free)
   - Alternatives: PyCharm, Sublime Text, or any text editor

3. **Terminal/Command Prompt**
   - Windows: Command Prompt or PowerShell
   - macOS: Terminal
   - Linux: Terminal

### Required API Keys

You'll need three free API keys:
- **OpenAI API Key** (for GPT-4o)
- **Tavily API Key** (for web search)
- **SERP API Key** (for flight/hotel search)

Don't worry, we'll show you how to get these later!

---

## 2. Understanding the Project Structure

Before we start, let's understand what each folder and file does:

```
multi_agent_travel_planner/          # Main project folder
│
├── main.py                          # 🚀 START HERE - The main program
│   └─ What it does: Entry point, runs the chatbot
│
├── requirements.txt                 # 📦 List of packages to install
│   └─ What it does: Tells pip what libraries to download
│
├── .env.example                     # 🔑 Template for your API keys
│   └─ What it does: Shows you what keys you need
│
├── .env                            # 🔒 YOUR SECRET KEYS (you'll create this)
│   └─ What it does: Stores your actual API keys
│
├── config/                         # ⚙️ Configuration files
│   └── settings.py                 # Loads API keys from .env file
│
├── src/                           # 🧠 Core application logic
│   ├── state.py                   # Defines data structure passed between agents
│   ├── router.py                  # Decides which agent handles the query
│   └── graph_builder.py           # Connects all agents together
│
├── agents/                        # 🤖 The three specialist agents
│   ├── itinerary_agent.py        # Plans trips and itineraries
│   ├── flight_agent.py           # Searches for flights
│   └── hotel_agent.py            # Searches for hotels
│
└── tools/                         # 🔧 External API integrations
    ├── tavily_search.py          # Web search functionality
    ├── flight_search.py          # Flight search via Google Flights
    └── hotel_search.py           # Hotel search via Google Hotels
```

### How It All Works Together

```
1. User types a query → main.py
                         ↓
2. Query goes to router.py (decides: flight? hotel? itinerary?)
                         ↓
3. Router sends to appropriate agent (flight_agent.py, hotel_agent.py, or itinerary_agent.py)
                         ↓
4. Agent uses tools (flight_search.py, hotel_search.py, tavily_search.py)
                         ↓
5. Agent sends response back to user
```

---

## 3. Step-by-Step Setup

### Step 1: Open Terminal/Command Prompt

**Windows:**
- Press `Win + R`, type `cmd`, press Enter
- OR search for "Command Prompt" in Start menu

**macOS/Linux:**
- Press `Cmd + Space`, type "Terminal", press Enter
- OR find Terminal in Applications

### Step 2: Navigate to the Project Directory

```bash
# Use 'cd' (change directory) to navigate
cd path/to/multi_agent_travel_planner

# Example on Windows:
cd C:\Users\YourName\Documents\multi_agent_travel_planner

# Example on macOS/Linux:
cd ~/Documents/multi_agent_travel_planner

# Tip: You can drag the folder into terminal to auto-fill the path!
```

Verify you're in the right place:
```bash
# Windows
dir

# macOS/Linux
ls

# You should see: main.py, requirements.txt, README.md, etc.
```

### Step 3: Create a Virtual Environment

**What is a virtual environment?**
- It's an isolated space for your project's packages
- Prevents conflicts with other Python projects
- Think of it as a separate "room" for this project

**Creating the virtual environment:**

**Windows:**
```bash
# Create virtual environment named 'venv'
python -m venv venv

# Activate it
venv\Scripts\activate

# You'll see (venv) appear in your prompt:
# (venv) C:\Users\YourName\...>
```

**macOS/Linux:**
```bash
# Create virtual environment named 'venv'
python3 -m venv venv

# Activate it
source venv/bin/activate

# You'll see (venv) appear in your prompt:
# (venv) username@computer:~$
```

**Important Notes:**
- ✅ You MUST activate the virtual environment every time you open a new terminal
- ✅ When done working, type `deactivate` to exit
- ✅ The `venv` folder will be created in your project directory (don't delete it!)

### Step 4: Install Required Packages

Now we'll install all the libraries our project needs:

```bash
# Make sure virtual environment is activated (you see (venv) in prompt)
pip install -r requirements.txt

# This will install:
# - langchain (LLM framework)
# - langgraph (multi-agent workflows)
# - openai (GPT-4o access)
# - tavily-python (web search)
# - serpapi (flight/hotel search)
# - python-dotenv (for loading .env files)
# - and more...

# This may take 2-5 minutes
```

**What's happening?**
- `pip` is Python's package installer
- `-r requirements.txt` tells pip to read the list from that file
- Each package is downloaded from the internet and installed

### Step 5: Set Up Your API Keys

#### 5.1: Create the .env File

```bash
# Copy the example file to create your .env file

# Windows (Command Prompt)
copy .env.example .env

# Windows (PowerShell)
Copy-Item .env.example .env

# macOS/Linux
cp .env.example .env
```

#### 5.2: Open .env in a Text Editor

**Using VS Code:**
```bash
code .env
```

**Or open manually:**
- Right-click `.env` → Open with → Notepad/TextEdit/VS Code

#### 5.3: Add Your API Keys

The file will look like this:
```bash
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
```

Replace `your_openai_api_key_here` with your actual keys (see next section).

**Important:**
- ❌ No spaces around the `=` sign
- ❌ No quotes around the keys (unless they have spaces)
- ✅ One key per line
- ✅ Save the file after editing

---

## 4. Getting API Keys

### OpenAI API Key (for GPT-4o)

1. **Go to**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

2. **Sign in or create an account**
   - You may need to verify your email
   - You might need to add a payment method (it's pay-as-you-go)

3. **Create a new key**
   - Click "Create new secret key"
   - Give it a name like "Travel Planner"
   - Copy the key immediately (you can't see it again!)

4. **Add to .env**
   ```bash
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
   ```

**Cost:** Approximately $0.01-0.05 per query depending on length

### Tavily API Key (for web search)

1. **Go to**: [https://app.tavily.com/home](https://app.tavily.com/home)

2. **Sign up**
   - Use your email or Google account
   - Free tier: 1,000 searches/month

3. **Get your key**
   - Navigate to "API Keys" section
   - Copy your API key

4. **Add to .env**
   ```bash
   TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxx
   ```

### SERP API Key (for flights & hotels)

1. **Go to**: [https://serpapi.com/dashboard](https://serpapi.com/dashboard)

2. **Sign up**
   - Create a free account
   - Free tier: 100 searches/month

3. **Get your key**
   - Your private API key is shown on the dashboard
   - Copy it

4. **Add to .env**
   ```bash
   SERPAPI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

### Your Final .env File Should Look Like:

```bash
OPENAI_API_KEY=sk-proj-abc123xyz789...
TAVILY_API_KEY=tvly-def456uvw012...
SERPAPI_API_KEY=ghi789rst345...
```

---

## 5. Running the Application

### First Run: Interactive Chat Mode

```bash
# Make sure:
# 1. Virtual environment is activated (venv)
# 2. You're in the project directory
# 3. .env file has all API keys

python main.py
```

**What you'll see:**
```
============================================================
🚀 Initializing Multi-Agent Travel Planner
============================================================
✅ All API keys loaded successfully!
🤖 Initializing GPT-4o...
🔨 Building multi-agent travel planner graph...
✅ Travel planning graph built successfully!
📊 Graph visualization saved to travel_graph.png
============================================================
💬 Multi-Agent Travel Assistant (Interactive Mode)
============================================================
How to use:
- Ask about flights: 'Find flights from NYC to London'
- Ask about hotels: 'Find hotels in Paris'
- Ask about itineraries: 'Plan a 5-day trip to Japan'
- Type 'quit' to exit
============================================================

🧑 You: _
```

### Try These Example Queries:

**Flight Query:**
```
🧑 You: Find flights from New York to London on December 1st 2025

🧭 Router analyzing: 'Find flights from New York to London on December 1s...'
🎯 Router decision: FLIGHT → flight_agent
📊 Processing your query...
🤖 Assistant:
[Flight results will appear here...]
```

**Hotel Query:**
```
🧑 You: Find a hotel in Paris for December 1-5

🧭 Router analyzing: 'Find a hotel in Paris for December 1-5'
🎯 Router decision: HOTEL → hotel_agent
📊 Processing your query...
🤖 Assistant:
[Hotel results will appear here...]
```

**Itinerary Query:**
```
🧑 You: Plan a 3-day trip to Rome

🧭 Router analyzing: 'Plan a 3-day trip to Rome'
🎯 Router decision: ITINERARY → itinerary_agent
📊 Processing your query...
🤖 Assistant:
[Itinerary will appear here...]
```

**To Exit:**
```
🧑 You: quit

👋 Thank you for using the Multi-Agent Travel Planner!
```

### Single Query Mode

You can also run a single query from the command line:

```bash
python main.py "Find flights from NYC to Tokyo on 2025-12-01"
```

This is useful for testing or if you only need one answer.

---

## 6. Understanding the Code

### Key Concepts for Beginners

#### 1. **What is a "State"?**
In `src/state.py`, we define a `TravelPlannerState`:
```python
class TravelPlannerState(TypedDict):
    messages: List[BaseMessage]  # Conversation history
    next_agent: Optional[str]    # Which agent to route to
    user_query: Optional[str]    # Current query
```

**Think of it as:** A package that gets passed between agents, containing all the information they need.

#### 2. **What is an "Agent"?**
An agent is a specialized AI that handles specific tasks. We have three:

- **Itinerary Agent** (`agents/itinerary_agent.py`): Travel planning expert
- **Flight Agent** (`agents/flight_agent.py`): Flight booking expert  
- **Hotel Agent** (`agents/hotel_agent.py`): Hotel search expert

Each agent has:
- A **system prompt** (instructions on how to behave)
- **Tools** (functions it can call, like web search)
- A **node function** (how it processes queries)

#### 3. **What is the "Router"?**
The router (`src/router.py`) is like a receptionist:
- Reads the user's query
- Decides which specialist agent should handle it
- Sends the query to that agent

#### 4. **What is "LangGraph"?**
LangGraph is a framework for building multi-agent workflows. It:
- Connects agents in a graph (visual workflow)
- Manages state between agents
- Handles conversation memory

Our graph looks like:
```
START → Router → [Flight/Hotel/Itinerary Agent] → END
```

#### 5. **What are "Tools"?**
Tools are functions agents can call to get information:
- `tavily_search.py`: Web search
- `flight_search.py`: Google Flights API
- `hotel_search.py`: Google Hotels API

When an agent needs information, it "calls a tool" to fetch it.

---

## 7. Colab vs Local Development

### Understanding the Differences

| Aspect | Google Colab | Local (VS Code) |
|--------|--------------|-----------------|
| **Setup** | None needed | Manual setup required |
| **Environment** | Managed by Google | Virtual environment (venv) |
| **API Keys** | `userdata.get('KEY_NAME')` | `.env` file with `python-dotenv` |
| **Installation** | `!pip install package` | `pip install package` |
| **File Structure** | Single notebook (.ipynb) | Multiple .py files |
| **Persistence** | Session-based (resets) | Saved on your computer |
| **Debugging** | Basic | Advanced (breakpoints, etc.) |
| **Internet** | Always on | Need connection for APIs |

### Key Code Changes from Colab to Local

#### 1. API Key Loading
**Colab:**
```python
from google.colab import userdata
os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")
```

**Local:**
```python
from dotenv import load_dotenv
load_dotenv()  # Loads from .env file automatically
# Now all keys are in os.environ
```

#### 2. Package Installation
**Colab:**
```python
!pip install langchain  # ! prefix for shell commands
```

**Local:**
```bash
pip install langchain  # Run in terminal, no ! prefix
```

#### 3. File Structure
**Colab:**
- Everything in one notebook
- Cells executed in order
- Mix of code, markdown, outputs

**Local:**
- Separate .py files for each component
- Import statements to connect files
- Run with `python main.py`

#### 4. Imports
**Colab:**
```python
# Can import anywhere in notebook
from langchain import X
# ... some cells later ...
from langchain import Y
```

**Local:**
```python
# All imports at top of file
from langchain import X
from langchain import Y
# ... rest of code ...
```

---

## 8. Troubleshooting

### Common Errors and Solutions

#### Error: "No module named 'langchain'"

**Problem:** Package not installed or virtual environment not activated

**Solution:**
```bash
# 1. Check if venv is activated (you should see (venv) in prompt)
# If not, activate it:
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# 2. Install packages
pip install -r requirements.txt
```

#### Error: "API key 'OPENAI_API_KEY' not found"

**Problem:** Missing or incorrect .env file

**Solutions:**
1. **Check if .env exists:**
   ```bash
   # Windows
   dir .env
   
   # Mac/Linux
   ls -la .env
   ```

2. **Check .env content:**
   - Open .env in text editor
   - Verify all three keys are present
   - No extra spaces: `KEY=value` not `KEY = value`
   - Keys should start on column 1 (no indentation)

3. **Check .env location:**
   - Must be in same directory as main.py
   - Not in a subdirectory

#### Error: "ModuleNotFoundError: No module named 'src'"

**Problem:** Running from wrong directory

**Solution:**
```bash
# Navigate to project root (where main.py is)
cd /path/to/multi_agent_travel_planner

# Then run
python main.py
```

#### Error: "pip: command not found"

**Problem:** Python not properly installed or not in PATH

**Solution:**
- Try `python -m pip` instead of `pip`
- Or reinstall Python and check "Add to PATH"

#### Error: "Permission denied"

**Problem:** Don't have write permissions

**Solution:**
- **Don't use sudo!** That can cause issues
- Check folder permissions
- Try running terminal as administrator (Windows) or use `sudo` only if necessary (Mac/Linux)

#### Application runs but gets no results

**Problem:** API issues or wrong API keys

**Checks:**
1. Verify API keys are valid (try them in the respective dashboards)
2. Check you have credits/quota remaining
3. Check internet connection
4. Look for error messages in the terminal output

#### Virtual Environment Issues

**Forgot to activate venv:**
- You must activate it each time you open a new terminal
- Look for `(venv)` in your prompt

**Want to deactivate:**
```bash
deactivate
```

**Want to delete and recreate venv:**
```bash
# Deactivate first
deactivate

# Delete the venv folder
# Windows
rmdir /s venv

# Mac/Linux  
rm -rf venv

# Create fresh venv
python -m venv venv

# Activate and reinstall
# (follow Step 3 instructions above)
```

---

## 🎉 You're Ready!

You now have:
- ✅ A complete understanding of the project structure
- ✅ A working virtual environment
- ✅ All dependencies installed
- ✅ API keys configured
- ✅ Knowledge of how to run the application
- ✅ Understanding of key concepts
- ✅ Troubleshooting skills

### Next Steps:

1. **Try the application** with different queries
2. **Experiment** with the code (try changing prompts in agent files)
3. **Read the code** to understand how each part works
4. **Build something new** - add a restaurant agent, a weather agent, etc.

### Learning Resources:

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)

**Happy Coding! 🚀**

---

*If you're stuck, read the error message carefully - it usually tells you what's wrong!*
