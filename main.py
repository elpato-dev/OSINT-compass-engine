import os
from functools import wraps
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Importing modules
from emailgetter import get_email_data
from domaingetter import get_domain_data
from termgetter import get_term_data
from snscraper import get_snc_twitter_results, get_snc_facebook_results
from alertsetter import set_alert

# API Key functionality
load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.args.get('apikey') != API_KEY:
            return jsonify({'error': 'Invalid API key.'}), 403
        return view_function(*args, **kwargs)
    return decorated_function

# API definition
@app.route('/', methods=['GET'])
def home_endpoint():
    return("This is the OSINT-compass API")

@app.route('/term', methods=['GET'])
@require_api_key
def term_endpoint():
    term = request.args.get('term')
    news_count = request.args.get('news_count', default=10)
    tweet_count = request.args.get('tweet_count', default=10)
    if not term:
        return jsonify({'error': 'term argument is required.'}), 400
    result = get_term_data(term, news_count=news_count, tweet_count=tweet_count)
    return jsonify(result)

@app.route('/domain', methods=['GET'])
@require_api_key
def domain_endpoint():
    domain = request.args.get('domain')
    if not domain:
        return jsonify({'error': 'domain argument is required.'}), 400
    result = get_domain_data(domain)
    return jsonify(result)

@app.route('/email', methods=['GET'])
@require_api_key
def email_endpoint():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'email argument is required.'}), 400
    result = get_email_data(email)
    return jsonify(result)

@app.route('/alert', methods=['POST'])
@require_api_key
def alert_endpoint():
    term = request.form.get('term')
    channel = request.form.get('channel')
    contact = request.form.get('contact')
    scoregt = request.form.get('scoregt')
    scorelt = request.form.get('scorelt')
    scorechange = request.form.get('scorechange')

    if not term or not channel or not contact or (not scoregt and not scorelt and not scorechange):
        return jsonify({'error': 'Not enough arguments provided.'}), 400

    result = set_alert(term, channel, contact, scoregt, scorelt, scorechange)
    return jsonify(result)

@app.route('/snscrape', methods=['GET'])
@require_api_key
def snscrape():
    term = request.args.get('term')
    if not term:
        return "A term must be specified."

    entries = request.args.get('entries')
    if not entries:
        entries = 10
    else:
        entries = int(entries)

    twitter = request.args.get('twitter')
    if twitter and twitter.lower() == 'true':
        twitter = True
    else:
        twitter = False

    facebook = request.args.get('facebook')
    if facebook and facebook.lower() == 'true':
        facebook = True
    else:
        facebook = False

    results = []
    if twitter:
        results.extend(get_snc_twitter_results(term, entries))
    if facebook:
        results.extend(get_snc_facebook_results(term, entries))

    return jsonify(results)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Remove before deploying to render
#if __name__ == '__main__':
#    app.run()
