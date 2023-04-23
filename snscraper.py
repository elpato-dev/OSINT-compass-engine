from flask import jsonify
from snscrape.modules.reddit import RedditSearchScraper, RedditUserScraper, RedditSubredditScraper
import snscrape.modules.reddit
from snscrape.modules.mastodon import MastodonProfileScraper
import snscrape.modules.mastodon
from sentiment_analyzer import get_text_sentiment

def get_snc_reddit_results(term, entries, submissions, comments, searchtype):
    try:
        if searchtype == "term":
            scraper = RedditSearchScraper(name=term, submissions=submissions, comments=comments)
        elif searchtype == "user":
            scraper = RedditUserScraper(name=term, submissions=submissions, comments=comments)
        elif searchtype == "subreddit":
            scraper = RedditSubredditScraper(name=term, submissions=submissions, comments=comments)
        data = []
        results_sentiment = 0
        sentiment_count = 0
        for i, item in enumerate(scraper.get_items()):
            result = {}
            if type(item) is snscrape.modules.reddit.Comment:
                result["type"] = "comment"
                result["id"] = item.id
                result["author"] = item.author
                result["created"] = item.date
                result["subreddit"] = item.subreddit
                result["url"] = item.url
                result["parentId"] = item.parentId
                result["body"] = item.body
                results_sentiment = results_sentiment + get_text_sentiment(str(item.body))
                sentiment_count+=1          
            elif type(item) is snscrape.modules.reddit.Submission:
                result["type"] = "submission"
                result["title"] = item.title
                result["id"] = item.id
                result["author"] = item.author
                result["created"] = item.date
                result["selftext"] = item.selftext
                result["subreddit"] = item.subreddit
                result["url"] = item.url
                result["link"] = item.link
                results_sentiment = results_sentiment + get_text_sentiment(str(item.selftext))
                sentiment_count+=1
            data.append(result)
            if i > entries - 2:
                break
        term_data = {
            "content" : data,
            "sentiment" : results_sentiment/sentiment_count,
            "title": "reddit"
            }
        return term_data
    except Exception as e:
        return {"error": str(e)}
    