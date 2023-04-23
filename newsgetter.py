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

    try:
        news_response = requests.get(news_url)

        # Raise an exception for any HTTP error responses
        news_response.raise_for_status()

        news_json= news_response.json()
        articles = []
        for article in news_json["articles"]:
            articles.append({"source" : article["source"]["id"], "title": article["title"], "content" : article["content"], "url" : article["url"]})

        return({"articles" : articles, "count" : news_json["totalResults"]})

    except requests.exceptions.HTTPError as e:
        if news_response.status_code == 429:
            return {"error": "API rate limit exceeded. Please try again later."}
        elif news_response.status_code == 404:
            return {"error": "No results found for query."}
        else:
            return {"error": str(e)}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
