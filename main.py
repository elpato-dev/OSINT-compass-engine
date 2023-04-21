import os
from functools import wraps
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Importing modules
from emailgetter import get_email_data
from domaingetter import get_domain_data
from termgetter import get_term_data
from alertsetter import set_alert

# API Key functionality
load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        print(API_KEY)
        if request.args.get('apikey') != API_KEY:
            return jsonify({'error': 'Invalid API key.'}), 403
        return view_function(*args, **kwargs)
    return decorated_function

# API definition
@app.route('/term', methods=['GET'])
@require_api_key
def term_endpoint():
    term = request.args.get('term')
    if not term:
        return jsonify({'error': 'term argument is required.'}), 400
    result = get_term_data(term)
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

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Remove before deploying to render
#if __name__ == '__main__':

#    app.run()
