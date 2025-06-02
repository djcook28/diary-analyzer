import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
import os

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

filepaths = glob.glob("Diaries/*.txt")
filepaths.sort()

def analyze_content(text):
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['pos'], sentiment_score['neg']

def get_diary_sentiment():
    diary_scores = []

    for filepath in filepaths:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            file_name = os.path.splitext(os.path.basename(filepath))[0]
            pos, neg = analyze_content(content)
            diary_scores.append((file_name, pos, neg))

    return zip(*diary_scores)