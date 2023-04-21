import requests
from dotenv import load_dotenv
import os

load_dotenv()
news_api_token = os.getenv("NEWS_API_TOKEN")

def get_news(news_word, news_count=10):
    news_url = ('https://newsapi.org/v2/everything?'
        'q='+ news_word +'&'
        'sortBy=publishedAty&'
        'pageSize='+ str(news_count) +'&' +
        'apiKey=' + news_api_token)

    news_response = requests.get(news_url)
    news_json= news_response.json()
    articles = []
    for article in news_json["articles"]:
        articles.append({"source" : article["source"]["id"], "title": article["title"], "content" : article["content"], "url" : article["url"]})

    return({"articles" : articles, "count" : news_json["totalResults"]})

