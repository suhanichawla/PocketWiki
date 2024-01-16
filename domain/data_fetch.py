import requests
REQUEST_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

def download_articles(n=200):
    articles = {}
    article_links = {}
    for _ in range(n):
        response = requests.get(REQUEST_URL)
        if response.status_code == 200:
            data = response.json()
            title = data['title']
            content = data['extract']
            url = data['content_urls']['desktop']['page']
            articles[title] = content.lower()
            article_links[title] = url
    return articles, article_links
