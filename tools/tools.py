import os
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

def get_profile_url_tavily(name: str):
    """Searches for LinkedIn profile page and ensures it is in the correct format."""
    
    search = TavilySearchResults()
    res = search.run(f"{name}")
    
    # Iterate over the results to find the first valid /in/ LinkedIn URL
    for result in res:
        url = result["url"]
        if "/in/" in url:  # Check for the correct URL format
            return url  # Return the first valid URL

    raise ValueError("No valid LinkedIn /in/ URL found.")

if __name__ == "__main__":
    profile_url = get_profile_url_tavily(name="Sanya Nanda")
    print(f"LinkedIn Profile URL: {profile_url}")
