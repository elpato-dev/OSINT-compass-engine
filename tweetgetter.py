import requests
from dotenv import load_dotenv
import os

load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")
search_url = "https://api.twitter.com/2/tweets/search/recent"



def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_tweets(twitter_word, tweet_count=10):

    if bearer_token == None:
        return({})
    json_response = connect_to_endpoint(search_url, {'query': twitter_word, 'max_results': tweet_count})

    cleaned_tweets =[]
    for tweet_response in json_response["data"]:
        cleaned_tweets.append(tweet_response["text"])
    
    return(cleaned_tweets)


    



