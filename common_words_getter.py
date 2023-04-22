import nltk

def get_common_words(text_list):

    # Process the articles
    counts = {}
    for text in text_list:

        # Extract the company names
        tokens = nltk.word_tokenize(text)
        tagged = nltk.pos_tag(tokens)
        companies = [word for word, tag in tagged if tag == 'NNP']

        # Count the mentions of each company
        for company in companies:
            if company in counts:
                counts[company] += 1
            else:
                counts[company] = 1

    # Filter the results based on the conditions: minimum 3 mentions and 3 characters,
    # the word cannot start with a backslash or forward slash, and it has to include at least one alphabetic character
    filtered_counts = {company: count for company, count in counts.items() if count >= 3 and len(company) >= 3 and not company.startswith('\\') and not company.startswith('/') and any(c.isalpha() for c in company)}

    # Print the results
    sorted_counts = sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True)
    
    return(sorted_counts)
