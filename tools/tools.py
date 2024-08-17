import os
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

def get_profile_url_tavily(name: str):
    """Searches for Linkedin profile page"""

    search = TavilySearchResults()
    res = search.run(f"{name}")
    #print("hi")
    
    return res[0]["url"]
    
if __name__=="__main__":
    get_profile_url_tavily(name="Sanya Nanda")