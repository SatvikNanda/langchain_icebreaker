from dotenv import load_dotenv
import os

load_dotenv()  # Make sure the .env file is loaded

api_key = os.getenv("PROXY_API_KEY")  # Fetch the API key
print(f"API Key: {api_key}")  # Debugging: Print the API key to ensure it's loaded correctly
