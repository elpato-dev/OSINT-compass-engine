from flask import jsonify
from snscrape.modules.reddit import RedditSearchScraper, RedditUserScraper
import snscrape.modules.reddit
from sentiment_analyzer import get_text_sentiment


def get_snc_instagram_results(user, entries):
    # Implementierung der Funktionalität, um Daten von Twitter zu holen
    return ('success : instagram data.')

def get_snc_reddit_term_results(term, entries, submissions, comments):
    try:
        scraper = RedditSearchScraper(name=term, submissions=submissions, comments=comments)
        data = []
        results_sentiment = 0
        sentiment_count = 0
        for i, term in enumerate(scraper.get_items()):
            result = {}
            if type(term) is snscrape.modules.reddit.Comment:
                result["type"] = "comment"
                result["id"] = term.id
                result["author"] = term.author
                result["created"] = term.date
                result["subreddit"] = term.subreddit
                result["url"] = term.url
                result["parentId"] = term.parentId
                result["body"] = term.body
                results_sentiment = results_sentiment + get_text_sentiment(str(term.body))
                sentiment_count+=1          
            elif type(term) is snscrape.modules.reddit.Submission:
                result["type"] = "submission"
                result["title"] = term.title
                result["id"] = term.id
                result["author"] = term.author
                result["created"] = term.date
                result["selftext"] = term.selftext
                result["subreddit"] = term.subreddit
                result["url"] = term.url
                result["link"] = term.link
                results_sentiment = results_sentiment + get_text_sentiment(str(term.selftext))
                sentiment_count+=1
            data.append(result)
            if i > entries - 2:
                break
        term_data = {
            "sentiment" : results_sentiment/sentiment_count,
            "results" : data}
        return term_data
    except Exception as e:
        return {"error": str(e)}
    
def get_snc_reddit_user_results(user, entries, submissions, comments):
    try:
        scraper = RedditUserScraper(name=user, submissions=submissions, comments=comments)
        data = []
        results_sentiment = 0
        sentiment_count = 0
        for i, user in enumerate(scraper.get_items()):
            result = {}
            if type(user) is snscrape.modules.reddit.Comment:
                result["type"] = "comment"
                result["id"] = user.id
                result["author"] = user.author
                result["created"] = user.date
                result["subreddit"] = user.subreddit
                result["url"] = user.url
                result["parentId"] = user.parentId
                result["body"] = user.body
                results_sentiment = results_sentiment + get_text_sentiment(str(user.body))     
                sentiment_count+=1    
            elif type(user) is snscrape.modules.reddit.Submission:
                result["type"] = "submission"
                result["title"] = user.title
                result["id"] = user.id
                result["author"] = user.author
                result["created"] = user.date
                result["selftext"] = user.selftext
                result["subreddit"] = user.subreddit
                result["url"] = user.url
                result["link"] = user.link
                results_sentiment = results_sentiment + get_text_sentiment(str(user.selftext))
                sentiment_count+=1
            data.append(result)
            if i > entries - 2:
                break
        user_data = {
                "sentiment" : results_sentiment/sentiment_count,
                "results" : data}
        return user_data
    except Exception as e:
        return {"error": str(e)}