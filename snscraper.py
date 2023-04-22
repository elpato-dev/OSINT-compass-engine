from flask import jsonify
from snscrape.modules.reddit import RedditSearchScraper
import snscrape.modules.reddit

def get_snc_instagram_results(user, entries):
    # Implementierung der Funktionalität, um Daten von Twitter zu holen
    return ('success : instagram data.')

def get_snc_reddit_term_results(term, entries, submissions, comments):
    try:
        scraper = RedditSearchScraper(term, submissions=submissions, comments=comments)
        data = []
        for i, term in enumerate(scraper.get_items()):
            result = {}
            if type(term) is snscrape.modules.reddit.Comment:
                result["type"] = "comment"
                result["id"] = term.id
                result["author"] = term.author
                result["created"] = term.date
                result["subreddit"] = term.subreddit
                result["url"] = term.url
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
            data.append(result)
            if i > entries - 2:
                break
        return data
    except Exception as e:
        return {"error": str(e)}