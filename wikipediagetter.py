import requests

def get_wikipedia_data(wiki_word):
    wiki_url = ('https://en.wikipedia.org/w/api.php?'
        'action=opensearch&'
        'search='+wiki_word)

    wiki_response = requests.get(wiki_url)

    wiki_terms = wiki_response.json()[1]
    wiki_links = wiki_response.json()[3]
    wiki_term_index = 0
    wiki_list = []

    for wiki_term in wiki_terms:

        wiki_dict = {
            "title": wiki_term,
            "url": wiki_links[wiki_term_index]
        }

        wiki_term_index = wiki_term_index+1

        wiki_list.append(wiki_dict)

    return(wiki_list)