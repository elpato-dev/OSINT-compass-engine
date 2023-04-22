from tweetgetter import get_tweets
from newsgetter import get_news
from sentiment_analyzer import get_text_sentiment


def get_term_data(term, tweet_count=10, news_count=10):

    tweets_raw = get_tweets(term, tweet_count)
    news_raw = get_news(term, news_count)
    tweets_sentiment = 0
    articles_sentiment = 0

    if tweets_raw != {}:
        for tweet in tweets_raw:

            tweets_sentiment = tweets_sentiment + get_text_sentiment(tweet)

        tweets = {"tweets_text": tweets_raw,
                "sentiment": tweets_sentiment/tweet_count}
    else:
        tweets = {}
    
    for article in news_raw["articles"]:
        articles_sentiment = articles_sentiment + get_text_sentiment(article["content"])

    
    news = {
        "articles" : news_raw["articles"],
        "count" : news_raw["count"],
        "sentiment": articles_sentiment/news_count
    }


    term_data = {"tweets": tweets,
                 "news": news}
    
    return(term_data)