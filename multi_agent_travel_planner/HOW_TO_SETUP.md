# ✅ How to Create Virtual Environment & Install Requirements

## 🎯 Answer to Your Question

You asked: **"How do I create virtual env and install all requirement.txt before I start building anything?"**

### ⚡ Quick Answer (30 seconds)

**Just run ONE command:**

**Windows:**
```bash
cd multi_agent_travel_planner
setup.bat
```

**macOS/Linux:**
```bash
cd multi_agent_travel_planner
./setup.sh
```

**Done!** The script automatically:
- ✅ Creates virtual environment
- ✅ Activates it
- ✅ Installs ALL requirements
- ✅ Validates everything works
- ✅ Tells you what to do next

---

## 📋 What You'll See

When you run the setup script, you'll see:

```
==================================================
🚀 Multi-Agent Travel Planner - Setup Script
==================================================

✅ Found: Python 3.10.12

📦 Step 1/4: Creating virtual environment...
✅ Virtual environment created

📦 Step 2/4: Activating virtual environment...
✅ Virtual environment activated

📦 Step 3/4: Upgrading pip...
✅ Pip upgraded

📦 Step 4/4: Installing dependencies from requirements.txt...
ℹ️  This may take 2-5 minutes...
✅ All dependencies installed successfully!

==================================================
🎉 Setup Complete!
==================================================
```

---

## 🔧 Manual Method (If You Want to Understand Each Step)

### Step 1: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
```

**macOS/Linux:**
```bash
python3 -m venv venv
```

**What this does:** Creates an isolated Python environment in a folder called `venv`

### Step 2: Activate Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

**You'll know it worked:** Your prompt will show `(venv)` at the start

### Step 3: Install All Requirements

```bash
pip install -r requirements.txt
```

**What this installs:**
- langchain (LLM framework)
- langgraph (multi-agent workflows)
- openai (GPT-4o)
- tavily-python (web search)
- serpapi (flight/hotel search)
- python-dotenv (environment variables)
- And more...

**Time:** 2-5 minutes

### Step 4: Verify Installation

```bash
python test_setup.py
```

This checks that everything installed correctly!

---

## 📍 Where Are These Files?

```
multi_agent_travel_planner/
├── setup.sh              ← Automated setup (Mac/Linux)
├── setup.bat             ← Automated setup (Windows)
├── requirements.txt      ← List of all packages to install
├── test_setup.py        ← Validates your setup
└── ... (other files)
```

---

## 🎓 Understanding Virtual Environments

### What is a Virtual Environment?

Think of it like a separate "room" for your project:
- Has its own Python packages
- Doesn't interfere with other projects
- Can be deleted and recreated anytime

### Why Use Virtual Environments?

**Without venv:**
```
Your Computer
├── Python
├── Package A (version 1.0) ← Used by Project 1
└── Package A (version 2.0) ← Project 2 needs this! CONFLICT!
```

**With venv:**
```
Your Computer
├── Project 1/
│   └── venv/ → Package A v1.0 ✅
└── Project 2/
    └── venv/ → Package A v2.0 ✅
```

No conflicts! Each project has its own packages.

---

## 🚀 Complete Workflow (From Scratch to Running)

### 1. Initial Setup (First Time Only)

```bash
# Navigate to project
cd multi_agent_travel_planner

# Run automated setup
./setup.sh          # Mac/Linux
# OR
setup.bat          # Windows

# This creates venv and installs everything!
```

### 2. Configure API Keys (First Time Only)

```bash
# Copy template
cp .env.example .env

# Edit .env and add your keys:
# - OPENAI_API_KEY=sk-proj-...
# - TAVILY_API_KEY=tvly-...  
# - SERPAPI_API_KEY=...
```

### 3. Every Time You Work on the Project

```bash
# Activate virtual environment
source venv/bin/activate    # Mac/Linux
# OR
venv\Scripts\activate       # Windows

# Now you can run the app
python main.py

# When done, deactivate
deactivate
```

---

## 🆘 Common Issues

### "Python not found"
**Windows:** Download from https://python.org, check "Add to PATH"
**Mac:** `brew install python3` or download from python.org
**Linux:** `sudo apt install python3 python3-venv`

### "venv\Scripts\activate : cannot be loaded" (Windows PowerShell)
**Solution:** Run this once:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Or use Command Prompt instead

### "pip: command not found"
**Solution:** Use:
```bash
python -m pip install -r requirements.txt
```

### Virtual environment already exists
**Solution:** The setup script asks if you want to recreate it, or just activate existing one

---

## 📚 Additional Resources

Created just for you:

1. **`VENV_SETUP.md`** - Detailed venv guide
2. **`SETUP_GUIDE.md`** - Complete beginner guide (17,000 words!)
3. **`QUICK_REFERENCE.md`** - Command cheat sheet
4. **`README.md`** - Project overview

---

## ✅ Quick Checklist

Before you start building:

- [ ] Navigate to `multi_agent_travel_planner/`
- [ ] Run `setup.sh` or `setup.bat`
- [ ] Wait for "Setup Complete!"
- [ ] Copy `.env.example` to `.env`
- [ ] Add your API keys to `.env`
- [ ] Run `python test_setup.py` to verify
- [ ] See all ✅ green checkmarks
- [ ] You're ready to build! 🎉

---

## 🎉 Summary

**Your Question:** How do I create venv and install requirements?

**Answer:** Run `setup.sh` (Mac/Linux) or `setup.bat` (Windows)

**Time:** 30 seconds (+ 2-5 min for downloads)

**What it does:** Everything! Creates venv, installs packages, validates setup

**Next step:** Configure `.env` with API keys, then `python main.py`

---

**You're all set! Happy coding!** 🚀

For any issues, check `SETUP_GUIDE.md` or `VENV_SETUP.md`
