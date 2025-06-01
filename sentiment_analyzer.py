import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

def analyze_content(text):
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['pos'], sentiment_score['neg']