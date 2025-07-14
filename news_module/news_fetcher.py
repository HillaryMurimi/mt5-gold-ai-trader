import requests
import logging

class NewsFetcher:
    def __init__(self, api_key, query="Gold", language="en"):
        self.api_key = api_key
        self.query = query
        self.language = language
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_news(self, page_size=10):
        params = {
            "q": self.query,
            "language": self.language,
            "pageSize": page_size,
            "sortBy": "publishedAt",
            "apiKey": self.api_key
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            articles = response.json().get("articles", [])
            return [article["title"] + ". " + article["description"] for article in articles if article["description"]]
        except Exception as e:
            logging.error(f"Failed to fetch news: {e}")
            return []

if __name__ == '__main__':
    # Replace with your real API key
    API_KEY = "your_newsapi_key_here"
    fetcher = NewsFetcher(api_key=API_KEY)
    headlines = fetcher.fetch_news()
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}\n")
