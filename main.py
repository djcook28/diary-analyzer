import streamlit as st
import plotly.express as px
from sentiment_analyzer import get_diary_sentiment

dates, pos_score, neg_score = get_diary_sentiment()

st.title("Diary Tone")
st.subheader("Positivity")
fig = px.line(x=dates, y=pos_score)
st.plotly_chart(fig)

st.subheader("Negativity")
fig = px.line(x=dates, y=neg_score)
st.plotly_chart(fig)
