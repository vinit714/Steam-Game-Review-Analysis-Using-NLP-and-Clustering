# app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
from collections import Counter
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("steam_all_game_reviews_with_cleaned.csv")
    df["Cleaned Review"] = df["Cleaned Review"].astype(str)
    df["Review Length"] = df["Review"].astype(str).apply(len)
    return df

df = load_data()

st.title("🎮 Steam Game Review Analysis Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
appid_filter = st.sidebar.multiselect("Select AppID", options=df["AppID"].unique(), default=df["AppID"].unique()[:10])

filtered_df = df[df["AppID"].isin(appid_filter)]

# BUG Detection
error_keywords = [
    "bug", "bugs", "crash", "crashing", "crashed", "glitch", "glitches",
    "error", "issue", "lag", "lagging", "freezing", "freeze", "broken",
    "problem", "problems", "unplayable", "disconnect", "stuck", "slow"
]

filtered_df["is_bug"] = filtered_df["Cleaned Review"].apply(lambda x: any(kw in x for kw in error_keywords))
filtered_df["sentiment"] = filtered_df["Cleaned Review"].apply(lambda x: TextBlob(x).sentiment.polarity)
filtered_df["bug_sentiment"] = filtered_df.apply(lambda row: TextBlob(row["Cleaned Review"]).sentiment.polarity if row["is_bug"] else None, axis=1)

# ---- Overview ----
st.subheader("📌 Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", len(filtered_df))
col2.metric("Bug-Related Reviews", filtered_df["is_bug"].sum())
col3.metric("Games Selected", filtered_df["AppID"].nunique())

# Pie chart
bug_counts = filtered_df["is_bug"].value_counts()
fig1 = px.pie(values=bug_counts.values, names=["Non-Bug", "Bug"], title="Bug vs Non-Bug Reviews")
st.plotly_chart(fig1)

# ---- Review Length ----
st.subheader("✍️ Review Length Distribution")
fig2 = px.histogram(filtered_df, x="Review Length", nbins=30, title="Distribution of Review Lengths")
st.plotly_chart(fig2)

# ---- Common Words ----
st.subheader("🗣️ Most Frequent Words in Cleaned Reviews")
all_words = " ".join(filtered_df["Cleaned Review"]).split()
common_words = Counter(all_words).most_common(15)
words_df = pd.DataFrame(common_words, columns=["word", "count"])
fig3 = px.bar(words_df, x="word", y="count", title="Top 15 Words in Cleaned Reviews")
st.plotly_chart(fig3)

# ---- Bug WordCloud ----
st.subheader("☁️ Bug-Related WordCloud")
bug_words = " ".join(filtered_df[filtered_df["is_bug"]]["Cleaned Review"])
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(bug_words)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# ---- Top Buggy Games ----
st.subheader("🎯 Games with Most Bug Mentions")
bug_counts = filtered_df.groupby("AppID")["is_bug"].sum().sort_values(ascending=False).head(10)
fig4 = px.bar(bug_counts, title="Top 10 Games by Bug Mentions")
st.plotly_chart(fig4)

# ---- Bug Sentiment ----
st.subheader("📉 Bug Review Sentiment")
bug_sentiment_df = filtered_df.dropna(subset=["bug_sentiment"])
fig5 = px.histogram(bug_sentiment_df, x="bug_sentiment", nbins=30, title="Sentiment Polarity of Bug Reviews")
st.plotly_chart(fig5)

# ---- Review Clustering (PCA) ----
if "PCA1" in filtered_df.columns and "PCA2" in filtered_df.columns:
    st.subheader("🔍 Review Clusters (PCA Visualization)")
    fig6 = px.scatter(filtered_df, x="PCA1", y="PCA2", color="Review Cluster", hover_data=["AppID", "Review"])
    st.plotly_chart(fig6)
else:
    st.warning("PCA1 and PCA2 columns not found. Run clustering section first.")

