import streamlit
import streamlit as st
import plotly
from sentiment_analyzer import get_diary_sentiment

diary_scores = get_diary_sentiment()

streamlit.title("Diary Tone")

streamlit.subheader("Positivity")

streamlit.subheader("Negativity")
