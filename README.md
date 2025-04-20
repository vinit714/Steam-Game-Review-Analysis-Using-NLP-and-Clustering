# 🎮 Steam Game Review Analysis Using NLP and Clustering

This project uses real user reviews from the Steam gaming platform to detect bug-related feedback using Natural Language Processing (NLP), perform sentiment analysis, and visualize insights through clustering and dashboards.

 ## Problem Statement:

The gaming industry is witnessing exponential growth, with thousands of titles being released on platforms like Steam every year. However, alongside this growth, game developers face mounting challenges with bug management, performance issues, and user satisfaction, especially when negative experiences are shared through player reviews.

This project aims to address the following key problem:

> "How can Natural Language Processing (NLP) and Data Analytics be used to detect, categorize, and visualize bug/error-related issues in Steam games, and how do these issues correlate with game attributes such as price, tags, publishers, and release timeline?"


## 📌 Project Objectives
- Collect reviews for top Steam games using AppIDs.
- Clean and preprocess text data.
- Detect bug-related reviews using keyword filtering.
- Perform sentiment analysis (positive, negative, neutral).
- Group games using clustering based on review content.
- Visualize insights using Matplotlib, Seaborn, and Streamlit.

## 🛠️ Technologies Used
- Python
- Pandas, Numpy
- NLTK, TextBlob, Scikit-learn
- TF-IDF, KMeans, PCA
- Matplotlib, Seaborn, Plotly
- Streamlit

> !! Note that not all dataset is uploaded to the repo, but you can scrape and filter your own data by running the project in the following order Scrapper.ipynnb -> clean_dataset.ipyn -> game review analysis.ipynb to check if the code is working or not -> steam game bug analysis.ipynb -> eda.ipynb -> app.py

