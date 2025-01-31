#Day 30
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        print("Sentiment: Positive")
    elif polarity < 0:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")

text = "This is an amazing product!"
analyze_sentiment(text)

text = "I hate this movie."
analyze_sentiment(text)

text = "The weather is okay today."
analyze_sentiment(text)
