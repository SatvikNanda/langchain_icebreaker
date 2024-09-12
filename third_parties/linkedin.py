from dotenv import load_dotenv
import os
import requests

#print(os.getenv("PROXY_API_KEY"))


# Load environment variables from .env file
load_dotenv()

def scrape_linkedin_profile(Linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn profiles using Proxycurl API."""
    
    if mock:
        Linkedin_profile_url = "https://gist.githubusercontent.com/SatvikNanda/86474ecb5403f31f67a180a19df5e992/raw/ae3f154ee199aab5d13fcc8195eb9e503237d13a/sanya-nanda.json"
        response = requests.get(Linkedin_profile_url, timeout=10)
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        header_dic = {'Authorization': f'Bearer {os.getenv("PROXY_API_KEY")}'}
        
        try:
            response = requests.get(
                api_endpoint,
                params={'linkedin_profile_url': Linkedin_profile_url},
                headers=header_dic,
                timeout=10
            )
            response.raise_for_status()  # Raises HTTPError for bad responses
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Response content: {response.text}")
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.RequestException as err:
            print(f"Request error occurred: {err}")
            return f"Request error occurred: {err}"

    if response.status_code == 200:
        data = response.json()
        # Compressing data variable by removing unnecessary fields
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
        }
        return data
    else:
        return f"Error: Received status code {response.status_code} from the API."

if __name__ == "__main__":
    print(scrape_linkedin_profile(Linkedin_profile_url="https://www.linkedin.com/in/sanya-nanda-aba12218b/", mock=True))
