# ⚡ Quick Reference Card

Quick commands and tips for working with the Multi-Agent Travel Planner.

---

## 🚀 Setup Commands

```bash
# 1. Navigate to project
cd multi_agent_travel_planner

# 2. Create virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup API keys
cp .env.example .env
# Edit .env with your API keys

# 5. Test setup
python test_setup.py

# 6. Run application
python main.py
```

---

## 📁 Project Structure Quick Map

```
multi_agent_travel_planner/
├── main.py                    → Start here to run
├── test_setup.py             → Test your setup
├── requirements.txt          → Dependencies list
├── .env                      → Your API keys (create this)
├── .env.example             → Template for API keys
│
├── README.md                → Overview & quick start
├── SETUP_GUIDE.md          → Detailed beginner guide
├── TUTORIAL.md             → Learn how it works
├── QUICK_REFERENCE.md      → This file
│
├── config/
│   └── settings.py         → Loads environment variables
│
├── src/
│   ├── state.py           → State definition
│   ├── router.py          → Query routing logic
│   └── graph_builder.py   → Builds the workflow graph
│
├── agents/
│   ├── itinerary_agent.py → Travel planning
│   ├── flight_agent.py    → Flight search
│   └── hotel_agent.py     → Hotel search
│
└── tools/
    ├── tavily_search.py   → Web search
    ├── flight_search.py   → Google Flights API
    └── hotel_search.py    → Google Hotels API
```

---

## 🔑 API Keys Quick Guide

| Service | URL | Free Tier |
|---------|-----|-----------|
| OpenAI | https://platform.openai.com/api-keys | Pay-as-you-go (~$0.01-0.05/query) |
| Tavily | https://app.tavily.com/home | 1,000 searches/month |
| SERP API | https://serpapi.com/dashboard | 100 searches/month |

**Add to .env file:**
```bash
OPENAI_API_KEY=sk-proj-...
TAVILY_API_KEY=tvly-...
SERPAPI_API_KEY=...
```

---

## 💡 Usage Examples

### Interactive Mode
```bash
python main.py

You: Find flights from NYC to London on 2025-12-01
You: Find hotels in Paris for 3 nights
You: Plan a 5-day trip to Tokyo
You: quit
```

### Single Query Mode
```bash
python main.py "Find flights from NYC to London"
```

---

## 🤖 Agent Routing Guide

| Keywords | Routes To | Handles |
|----------|-----------|---------|
| flight, airline, fly, departure, arrival | **Flight Agent** | Flight searches, bookings |
| hotel, stay, accommodation, room, lodging | **Hotel Agent** | Hotel searches, recommendations |
| itinerary, plan, trip, visit, attractions | **Itinerary Agent** | Travel plans, destinations, activities |

---

## 🛠️ Common Commands

### Virtual Environment
```bash
# Activate
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Deactivate
deactivate

# Delete and recreate
# Windows: rmdir /s venv
# Mac/Linux: rm -rf venv
python -m venv venv
```

### Package Management
```bash
# Install all requirements
pip install -r requirements.txt

# Install single package
pip install package-name

# Update all packages
pip install --upgrade -r requirements.txt

# List installed packages
pip list

# Show package info
pip show package-name
```

### Git (if using version control)
```bash
# Check status
git status

# Add files
git add .

# Commit
git commit -m "Your message"

# Push
git push
```

---

## 🐛 Troubleshooting Quick Fixes

### "No module named X"
```bash
# Activate venv first!
pip install -r requirements.txt
```

### "API key not found"
```bash
# Check .env exists
ls .env  # or dir .env on Windows

# Verify keys in .env (no spaces around =)
OPENAI_API_KEY=your_key_here

# .env must be in same folder as main.py
```

### "Module not found: src"
```bash
# Run from project root (where main.py is)
cd multi_agent_travel_planner
python main.py
```

### Virtual environment not activating
```bash
# Windows PowerShell - enable scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Or use Command Prompt instead of PowerShell
```

---

## 📝 File Editing Tips

### Config Files
- **.env**: API keys, one per line, no spaces around `=`
- **requirements.txt**: Package names, one per line, with versions

### Python Files
- **Imports**: Always at top of file
- **Functions**: Define before using
- **Indentation**: 4 spaces (not tabs)
- **Comments**: Use `#` for single line, `"""` for multi-line

---

## 🎯 Key Files to Modify

### Change Agent Behavior
Edit: `agents/[agent_name]_agent.py`
Look for: System prompt in `create_[agent]_agent()`

### Change Routing Logic
Edit: `src/router.py`
Look for: Router prompt in `create_router()`

### Add New Tool
1. Create: `tools/my_new_tool.py`
2. Import in agent: `from tools.my_new_tool import my_function`
3. Bind to agent: `llm.bind_tools([existing_tool, my_function])`

### Change Graph Structure
Edit: `src/graph_builder.py`
Look for: `workflow.add_node()` and `workflow.add_edge()`

---

## 📊 Testing Checklist

- [ ] Virtual environment activated (`(venv)` in prompt)
- [ ] All packages installed (`pip list` shows langchain, etc.)
- [ ] .env file exists with all 3 API keys
- [ ] Running from project root (see main.py with `ls`)
- [ ] Python 3.8+ (`python --version`)
- [ ] Internet connection (for API calls)

---

## 🔗 Useful Links

- **Documentation**: See README.md
- **Setup Guide**: See SETUP_GUIDE.md
- **Tutorial**: See TUTORIAL.md
- **LangChain Docs**: https://python.langchain.com/
- **LangGraph Docs**: https://langchain-ai.github.io/langgraph/

---

## ⌨️ Keyboard Shortcuts (VS Code)

- `Ctrl + ~`: Open terminal
- `Ctrl + P`: Quick file open
- `Ctrl + Shift + P`: Command palette
- `Ctrl + /`: Toggle comment
- `F5`: Start debugging

---

## 💾 Backup Your Work

```bash
# Create backup of .env (DON'T commit to git!)
cp .env .env.backup

# Backup entire project
# Just copy the folder or use git
```

---

## 🎓 Learning Path

1. ✅ Setup (SETUP_GUIDE.md)
2. ✅ Run the app (README.md)
3. ✅ Understand concepts (TUTORIAL.md)
4. ✅ Read the code (start with main.py)
5. ✅ Modify prompts (agents/*.py)
6. ✅ Add a feature (TUTORIAL.md - Extending)
7. ✅ Build your own agent!

---

**Pro Tip**: Keep this file open while working! 📌

---

*Last updated: 2026-02-03*
