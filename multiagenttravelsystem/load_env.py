from pathlib import Path
from dotenv import load_dotenv
import os
import logging

# Load from multiagenttravelsystem/.env (not project root)
ROOT = Path(__file__).resolve().parent
print(f"[INFO] Loading .env from: {ROOT / '.env'}")
env_file = ROOT / ".env"
load_dotenv(env_file)

# Debug: show which path was attempted
if not env_file.exists():
    print(f"[WARNING] .env file not found at: {env_file}")
else:
    print(f"[INFO] Loaded .env from: {env_file}")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

print(f"Loaded OPENAI_API_KEY: {f'{OPENAI_API_KEY}' if OPENAI_API_KEY else 'not set'}")
print(f"Loaded SERPAPI_API_KEY: {f'{SERPAPI_API_KEY}' if SERPAPI_API_KEY else 'not set'}")
print(f"Loaded TAVILY_API_KEY: {f'{TAVILY_API_KEY}' if TAVILY_API_KEY else 'not set'}")

