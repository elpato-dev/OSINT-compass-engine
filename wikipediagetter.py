import requests

def get_wikipedia_data(wiki_word):
    wiki_url = ('https://en.wikipedia.org/w/api.php?'
        'action=opensearch&'
        'search='+wiki_word)

    wiki_response = requests.get(wiki_url)

    wiki_terms = wiki_response.json()[1]
    wiki_links = wiki_response.json()[3]
    wiki_term_index = 0
    wiki_results = {}
    for wiki_term in wiki_terms:
        wiki_results[wiki_term] = wiki_links[wiki_term_index]
        wiki_term_index = wiki_term_index+1

    return(wiki_results)