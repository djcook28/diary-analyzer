import glob
import os
import streamlit as st
import plotly
import sentiment_analyzer

filepaths = glob.glob("Diaries/*.txt")
filepaths.sort()

diary_scores = []

for filepath in filepaths:
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        file_name = os.path.splitext(os.path.basename(filepath))[0]
        pos, neg = sentiment_analyzer.analyze_content(content)
        diary_scores.append((file_name, pos, neg))

print(diary_scores)