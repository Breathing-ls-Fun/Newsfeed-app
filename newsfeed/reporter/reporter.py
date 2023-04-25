from newsapi import NewsApiClient

class Reporter:
    def __init__(self, key=None):
        self.api = NewsApiClient(api_key=key)

    def get_top_headlines(self):
        return self.api.get_top_headlines(language='en')

    def search_articles(self, keyword):
        return self.api.get_everything(q=keyword,language='en')

    def get_sources(self):
        return self.api.get_sources(language='en')