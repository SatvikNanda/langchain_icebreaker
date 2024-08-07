import os
import requests


def scrape_linkedin_profile(Linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinedIn profile"""

    if mock:
        Linkedin_profile_url = "https://gist.githubusercontent.com/SatvikNanda/86474ecb5403f31f67a180a19df5e992/raw/ae3f154ee199aab5d13fcc8195eb9e503237d13a/sanya-nanda.json"
        response = requests.get(
            Linkedin_profile_url,
            timeout=10,
        )

    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {'Authorization': f'Bearer {os.environ.get("Proxy_API_KEY")}'}
        
        response = requests.get(
                        api_endpoint,
                        params={"url": Linkedin_profile_url},
                        headers=header_dic,
                        timeout=10,
                        )
        
    data = response.json()
    #compressing data variable
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data




if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            Linkedin_profile_url="https://www.linkedin.com/in/sanya-nanda-aba12218b/", mock=True
        )
    )