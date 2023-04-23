from tweetgetter import get_tweets
from newsgetter import get_news
from sentiment_analyzer import get_text_sentiment
from wikipediagetter import get_wikipedia_data
from common_words_getter import get_common_words


def get_term_data(term, tweet_count=10, news_count=10):

    tweets_raw = get_tweets(term, tweet_count)
    wikipedia_data = get_wikipedia_data(term)
    tweets_sentiment = 0
    articles_sentiment = 0

    if tweets_raw != {}:
        for tweet in tweets_raw:
            tweets_sentiment = tweets_sentiment + get_text_sentiment(tweet)
        tweets = {"tweets_text": tweets_raw,
                "sentiment": tweets_sentiment/tweet_count}
    else:
        tweets = {}
    
    try:
        news_raw = get_news(term, news_count)
        for article in news_raw["articles"]:
            articles_sentiment = articles_sentiment + get_text_sentiment(article["content"])

        news = {
            "articles" : news_raw["articles"],
            "count" : news_raw["count"],
            "sentiment": articles_sentiment/news_count
        }

        textlist = []
        for tweet_text in tweets_raw:
            textlist.append(tweet_text)
        for article_text in news_raw["articles"]:
            if "We use cookies" not in article_text["content"]:
                textlist.append(article_text["content"])
            textlist.append(article_text["title"])

        common_words = get_common_words(textlist)

    except:
        news_raw = {}
        news = {}
        common_words = get_common_words(tweets_raw)

    term_data = {"tweets": tweets,
                 "news": news,
                 "wikipedia": wikipedia_data,
                 "common_words": common_words}
    
    return(term_data)
