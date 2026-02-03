# 🚀 QUICK SETUP - Virtual Environment & Requirements

## TL;DR - One Command Setup

### Windows
```bash
cd multi_agent_travel_planner
setup.bat
```

### macOS/Linux
```bash
cd multi_agent_travel_planner
chmod +x setup.sh
./setup.sh
```

**That's it!** The script handles everything automatically.

---

## What the Setup Script Does

1. ✅ **Checks Python** - Verifies Python 3.8+ is installed
2. ✅ **Creates venv** - Sets up isolated virtual environment
3. ✅ **Activates venv** - Enables the environment
4. ✅ **Upgrades pip** - Updates package manager
5. ✅ **Installs packages** - Installs all requirements.txt dependencies
6. ✅ **Validates setup** - Runs test_setup.py to verify installation
7. ✅ **Guides API keys** - Reminds you to configure .env file

---

## Manual Setup (If You Prefer)

### Step 1: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
```

**macOS/Linux:**
```bash
python3 -m venv venv
```

**What this does:** Creates a folder called `venv` with isolated Python environment

### Step 2: Activate Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

**You'll see:** `(venv)` appears at the start of your command prompt

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

**What this does:** Installs all packages listed in requirements.txt:
- langchain
- langgraph
- openai
- tavily-python
- serpapi
- python-dotenv
- and more...

**Time:** 2-5 minutes depending on internet speed

### Step 4: Verify Installation

```bash
python test_setup.py
```

**What this does:** Checks that all packages installed correctly

---

## After Setup - Configure API Keys

### Step 1: Copy Template
```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

### Step 2: Edit .env File
Open `.env` in your text editor and add your keys:

```bash
OPENAI_API_KEY=sk-proj-your_actual_key_here
TAVILY_API_KEY=tvly-your_actual_key_here
SERPAPI_API_KEY=your_actual_key_here
```

### Step 3: Get API Keys

| Service | URL | Free Tier |
|---------|-----|-----------|
| **OpenAI** | https://platform.openai.com/api-keys | Pay-as-you-go (~$0.01/query) |
| **Tavily** | https://app.tavily.com/home | 1,000 searches/month |
| **SERP API** | https://serpapi.com/dashboard | 100 searches/month |

---

## Common Issues & Solutions

### Issue: "python3: command not found" (macOS/Linux)
**Solution:** Try `python` instead of `python3`, or install Python 3.8+

### Issue: "Python is not installed" (Windows)
**Solution:** Download from https://python.org/downloads/ and check "Add to PATH"

### Issue: "venv\Scripts\activate: cannot be loaded" (Windows PowerShell)
**Solution:** 
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Or use Command Prompt instead of PowerShell

### Issue: "pip: command not found"
**Solution:** 
```bash
python -m pip install -r requirements.txt
```

### Issue: Virtual environment exists
**Solution:** Either:
- Use existing: Just activate it
- Recreate: Delete `venv` folder and create new one

---

## Verify Everything is Working

After setup, run:

```bash
# Make sure venv is active (you see "(venv)" in prompt)
python test_setup.py
```

You should see:
```
✅ Package imports
✅ Project structure  
✅ Environment file
✅ Basic functionality
```

---

## Next Steps

Once setup is complete:

```bash
# Run the application
python main.py

# Try a query
You: Find flights from NYC to London

# Exit
You: quit
```

---

## Quick Reference

### Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Deactivate Virtual Environment
```bash
deactivate
```

### Install New Package
```bash
pip install package-name
```

### Update Requirements File
```bash
pip freeze > requirements.txt
```

### Delete Virtual Environment
```bash
# Deactivate first
deactivate

# Then delete
# Windows: rmdir /s venv
# macOS/Linux: rm -rf venv
```

---

## Need More Help?

- **Quick start**: See `README.md`
- **Detailed guide**: See `SETUP_GUIDE.md` (17,000 words!)
- **Commands**: See `QUICK_REFERENCE.md`
- **Concepts**: See `TUTORIAL.md`

---

**Last Updated:** 2026-02-03
