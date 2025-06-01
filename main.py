import glob
import streamlit as st
import plotly
import sentiment_analyzer

filepaths = glob.glob("Diaries/*.txt")
filepaths.sort()

diary_scores = []

for filepath in filepaths:
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        pos, neg = sentiment_analyzer.analyze_content(content)
        diary_scores.append((filepath, pos, neg))

print(diary_scores)