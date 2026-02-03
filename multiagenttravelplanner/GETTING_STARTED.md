# ✅ Getting Started Checklist
Use this checklist to set up and run your Multi-Agent Travel Planner. Check off each item as you complete it!
---
## 🎯 Pre-Setup Requirements
- [ ] Python 3.8 or higher installed
  - Check: `python --version` or `python3 --version`
  - If not installed: [Download Python](https://www.python.org/downloads/)
- [ ] A text editor or IDE installed
  - Recommended: [VS Code](https://code.visualstudio.com/)
  - Alternatives: PyCharm, Sublime Text, etc.
- [ ] Terminal/Command Prompt access
  - Windows: cmd, PowerShell, or Windows Terminal
  - macOS/Linux: Terminal app
- [ ] Internet connection (for API calls and package installation)
---
## 📦 Setup Steps
### Step 1: Project Navigation
- [ ] Open terminal/command prompt
- [ ] Navigate to project directory:
  ```bash
  cd /path/to/multi_agent_travel_planner
  ```
- [ ] Verify location (should see `main.py`):
  ```bash
  ls        # macOS/Linux
  dir       # Windows
  ```
### Step 2: Virtual Environment
- [ ] Create virtual environment:
  ```bash
  # Windows
  python -m venv venv
  
  # macOS/Linux
  python3 -m venv venv
  ```
- [ ] Activate virtual environment:
  ```bash
  # Windows (Command Prompt)
  venv\Scripts\activate
  
  # Windows (PowerShell)
  venv\Scripts\Activate.ps1
  
  # macOS/Linux
  source venv/bin/activate
  ```
- [ ] Verify activation (should see `(venv)` in prompt)
**Troubleshooting:**
- If PowerShell gives error: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- If stuck: Try Command Prompt instead of PowerShell
### Step 3: Install Dependencies
- [ ] Install all required packages:
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Wait for installation (2-5 minutes)
- [ ] Verify installation:
  ```bash
  pip list | grep langchain  # macOS/Linux
  pip list | findstr langchain  # Windows
  ```
**Expected packages:**
- langchain
- langchain-openai
- langchain-core
- langchain-community
- langgraph
- python-dotenv
- tavily-python
- google-search-results (serpapi)
### Step 4: Get API Keys
#### OpenAI API Key
- [ ] Go to: https://platform.openai.com/api-keys
- [ ] Sign in or create account
- [ ] Click "Create new secret key"
- [ ] Name it: "Travel Planner"
- [ ] Copy the key (starts with `sk-proj-...`)
- [ ] Save it somewhere safe (you can't see it again!)
**Cost:** ~$0.01-0.05 per query (pay-as-you-go)
#### Tavily API Key
- [ ] Go to: https://app.tavily.com/home
- [ ] Sign up (use email or Google)
- [ ] Navigate to "API Keys" section
- [ ] Copy your API key (starts with `tvly-...`)
**Free tier:** 1,000 searches per month
#### SERP API Key
- [ ] Go to: https://serpapi.com/dashboard
- [ ] Sign up for free account
- [ ] Copy your private API key from dashboard
- [ ] Note: This doesn't have a specific prefix
**Free tier:** 100 searches per month
### Step 5: Configure Environment
- [ ] Create `.env` file:
  ```bash
  # Windows (Command Prompt)
  copy .env.example .env
  
  # Windows (PowerShell)
  Copy-Item .env.example .env
  
  # macOS/Linux
  cp .env.example .env
  ```
- [ ] Open `.env` file in text editor
- [ ] Add your API keys (replace the placeholder text):
  ```bash
  OPENAI_API_KEY=sk-proj-your_actual_key_here
  TAVILY_API_KEY=tvly-your_actual_key_here
  SERPAPI_API_KEY=your_actual_key_here
  ```
- [ ] Save the file
**Important:**
- No spaces around `=` sign
- No quotes around keys (unless they contain spaces)
- One key per line
- File must be named exactly `.env` (with the dot)
### Step 6: Verify Setup
- [ ] Run the test script:
  ```bash
  python test_setup.py
  ```
- [ ] Check test results:
  - [ ] Package imports: ✅ All green
  - [ ] Project structure: ✅ All files found
  - [ ] Environment file: ✅ All keys present
  - [ ] Basic functionality: ✅ All imports work
**If any tests fail:**
- Read the error message carefully
- Check SETUP_GUIDE.md for troubleshooting
- Verify virtual environment is activated
- Confirm API keys are correct in `.env`
---
## 🚀 First Run
### Step 7: Launch the Application
- [ ] Make sure virtual environment is active (`(venv)` in prompt)
- [ ] Run the application:
  ```bash
  python main.py
  ```
- [ ] Wait for initialization messages:
  ```
  ✅ All API keys loaded successfully!
  🤖 Initializing GPT-4o...
  ✅ Travel planning graph built successfully!
  📊 Graph visualization saved to travel_graph.png
  ```
- [ ] See the chat prompt:
  ```
  🧑 You: _
  ```
### Step 8: Test with Example Queries
Try each type of query to test all agents:
#### Flight Query
- [ ] Type: `Find flights from New York to London on December 1st 2025`
- [ ] Press Enter
- [ ] Observe router decision: `FLIGHT → flight_agent`
- [ ] Wait for response (may take 10-30 seconds)
- [ ] Review flight results
#### Hotel Query
- [ ] Type: `Find a hotel in Paris for 3 nights`
- [ ] Press Enter
- [ ] Observe router decision: `HOTEL → hotel_agent`
- [ ] Wait for response
- [ ] Review hotel results
#### Itinerary Query
- [ ] Type: `Plan a 3-day trip to Rome`
- [ ] Press Enter
- [ ] Observe router decision: `ITINERARY → itinerary_agent`
- [ ] Wait for response
- [ ] Review itinerary suggestions
### Step 9: Multi-Turn Conversation Test
- [ ] Ask a follow-up question (uses conversation memory)
- [ ] Example: `What about the weather there?`
- [ ] Verify the system remembers previous context
### Step 10: Exit
- [ ] Type: `quit`
- [ ] See goodbye message
- [ ] Application closes
---
## 🎓 Learning & Exploration
### Documentation Review
- [ ] Read `README.md` for project overview
- [ ] Study `SETUP_GUIDE.md` for detailed explanations
- [ ] Go through `TUTORIAL.md` to understand concepts
- [ ] Keep `QUICK_REFERENCE.md` handy for commands
### Code Exploration
- [ ] Open `main.py` in your editor
- [ ] Follow the imports to other files
- [ ] Read inline comments
- [ ] Understand the flow
### Project Structure
- [ ] Review `PROJECT_STRUCTURE.md`
- [ ] Understand file organization
- [ ] See how modules connect
---
## 🔍 Verification Checklist
Before considering setup complete, verify:
- [ ] Virtual environment activates successfully
- [ ] All packages install without errors
- [ ] `.env` file has all three API keys
- [ ] `test_setup.py` shows all tests passed
- [ ] Application starts without errors
- [ ] Flight query returns results
- [ ] Hotel query returns results
- [ ] Itinerary query returns results
- [ ] Can quit the application cleanly
- [ ] `travel_graph.png` is created
---
## 🐛 Common Issues & Solutions
### Issue: Virtual environment won't activate
- [ ] Try different terminal (cmd vs PowerShell on Windows)
- [ ] Check Python installation
- [ ] Recreate venv: `rm -rf venv` then create again
### Issue: Package installation fails
- [ ] Update pip: `pip install --upgrade pip`
- [ ] Check internet connection
- [ ] Try installing packages one by one
### Issue: "API key not found"
- [ ] Verify `.env` exists in correct location
- [ ] Check for typos in API key names
- [ ] Ensure no extra spaces in `.env`
- [ ] Confirm keys are not wrapped in quotes
### Issue: "Module not found: src"
- [ ] Verify you're in project root directory
- [ ] Check that all `__init__.py` files exist
- [ ] Try: `cd multi_agent_travel_planner` then `python main.py`
### Issue: API calls fail
- [ ] Verify API keys are valid (test in respective dashboards)
- [ ] Check you have remaining quota
- [ ] Confirm internet connection
- [ ] Look for specific error messages