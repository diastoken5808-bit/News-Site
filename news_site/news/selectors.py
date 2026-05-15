import requests
from django.conf import settings

def get_news_list(query, num):
    url = "https://newsapi.org/v2/everything?domains=wsj.com"

    params = {
        'q': query,
        'pageSize': num,
        'sortBy': 'publishedAt',
        'language': 'en',
        'apiKey': settings.NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get('articles', [])