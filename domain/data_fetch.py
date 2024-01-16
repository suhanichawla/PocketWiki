import requests

def download_articles(n=200):
    articles = {}
    for _ in range(n):
        response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
        if response.status_code == 200:
            data = response.json()
            title = data['title']
            content = data['extract']
            articles[title] = content.lower()  # Convert to lowercase
    return articles
