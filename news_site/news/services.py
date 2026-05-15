import requests

class NewsAPI:
    BASE_URL = "https://newsapi.org/v2/everything?domains=wsj.com"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_news(self, query="technology", page_size=5):
        params = {
            "q": query,
            "pageSize": page_size,
            "apiKey": self.api_key,
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            return []

        return response.json().get("articles", [])