"""
Simple test script to verify the setup is correct.

This script checks:
1. All required packages are installed
2. All API keys are present
3. Basic imports work
"""

import sys
import os


def test_imports():
    """Test that all required packages can be imported."""
    print("📦 Testing package imports...")
    
    packages = [
        ("langchain", "LangChain"),
        ("langchain_openai", "LangChain OpenAI"),
        ("langchain_core", "LangChain Core"),
        ("langchain_community", "LangChain Community"),
        ("langgraph", "LangGraph"),
        ("dotenv", "Python Dotenv"),
        ("tavily", "Tavily"),
        ("serpapi", "SERP API"),
    ]
    
    failed = []
    for module, name in packages:
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - NOT INSTALLED")
            failed.append(name)
    
    if failed:
        print(f"\n❌ Missing packages: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n✅ All packages imported successfully!\n")
    return True


def test_env_file():
    """Test that .env file exists and has required keys."""
    print("🔑 Testing .env file...")
    
    if not os.path.exists('.env'):
        print("  ❌ .env file not found!")
        print("\nPlease:")
        print("  1. Copy .env.example to .env")
        print("  2. Add your API keys to .env")
        return False
    
    print("  ✅ .env file exists")
    
    # Load .env
    from dotenv import load_dotenv
    load_dotenv()
    
    # Check for required keys
    required_keys = [
        'OPENAI_API_KEY',
        'TAVILY_API_KEY', 
        'SERPAPI_API_KEY'
    ]
    
    missing = []
    for key in required_keys:
        value = os.environ.get(key)
        if not value or value.startswith('your_'):
            print(f"  ❌ {key} - NOT SET")
            missing.append(key)
        else:
            # Mask the key for security
            masked = value[:10] + "..." if len(value) > 10 else "***"
            print(f"  ✅ {key} - {masked}")
    
    if missing:
        print(f"\n❌ Missing API keys: {', '.join(missing)}")
        print("\nPlease add these keys to your .env file")
        print("See SETUP_GUIDE.md for instructions on getting API keys")
        return False
    
    print("\n✅ All API keys found!\n")
    return True


def test_project_structure():
    """Test that all required directories and files exist."""
    print("📁 Testing project structure...")
    
    required_paths = [
        'main.py',
        'requirements.txt',
        'config/settings.py',
        'src/state.py',
        'src/router.py',
        'src/graph_builder.py',
        'agents/itinerary_agent.py',
        'agents/flight_agent.py',
        'agents/hotel_agent.py',
        'tools/tavily_search.py',
        'tools/flight_search.py',
        'tools/hotel_search.py',
    ]
    
    missing = []
    for path in required_paths:
        if os.path.exists(path):
            print(f"  ✅ {path}")
        else:
            print(f"  ❌ {path} - NOT FOUND")
            missing.append(path)
    
    if missing:
        print(f"\n❌ Missing files: {', '.join(missing)}")
        print("\nMake sure you're running this from the project root directory")
        return False
    
    print("\n✅ All required files found!\n")
    return True


def test_basic_functionality():
    """Test that basic imports from our modules work."""
    print("🧪 Testing basic functionality...")
    
    try:
        from config.settings import load_config
        print("  ✅ Config module")
        
        from src.state import TravelPlannerState
        print("  ✅ State module")
        
        from src.router import create_router
        print("  ✅ Router module")
        
        from src.graph_builder import build_travel_planner_graph
        print("  ✅ Graph builder module")
        
        from agents.itinerary_agent import itinerary_agent_node
        from agents.flight_agent import flight_agent_node
        from agents.hotel_agent import hotel_agent_node
        print("  ✅ Agent modules")
        
        from tools.tavily_search import create_tavily_tool
        from tools.flight_search import search_flights
        from tools.hotel_search import search_hotels
        print("  ✅ Tool modules")
        
        print("\n✅ All modules can be imported!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ Import error: {e}")
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("🧪 Multi-Agent Travel Planner - Setup Test")
    print("=" * 60 + "\n")
    
    # Run tests
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Project Structure", test_project_structure()))
    results.append(("Environment File", test_env_file()))
    results.append(("Basic Functionality", test_basic_functionality()))
    
    # Summary
    print("=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{name}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 All tests passed! Your setup is ready!")
        print("\nNext steps:")
        print("  1. Run: python main.py")
        print("  2. Try some queries!")
        print("\nSee README.md for usage examples")
        return 0
    else:
        print("\n❌ Some tests failed. Please fix the issues above.")
        print("\nSee SETUP_GUIDE.md for detailed setup instructions")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
