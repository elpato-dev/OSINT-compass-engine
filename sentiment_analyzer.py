from textblob import TextBlob

def get_text_sentiment(text):
    text = TextBlob(text)
    return(text.sentiment.polarity)

