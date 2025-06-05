# Steam Game Review Analysis Using NLP & Clustering

This project analyzes real user reviews from Steam to detect bug-related feedback using Natural Language Processing (NLP), perform sentiment analysis, and visualize insights through clustering and interactive dashboards.

---

## Problem Statement

With the rapid growth of the gaming industry and frequent Steam releases, players often report performance issues, bugs, and errors in reviews. However, extracting actionable insights from this unstructured feedback is challenging.

This project addresses the problem:
> _How can NLP and data analytics be used to detect, categorize, and visualize bug/error-related reviews on Steam, and how do these issues relate to game features like tags, pricing, publishers, and release timelines?_

---

## Objectives

- Scrape reviews for top Steam games using AppIDs.
- Clean and preprocess raw review data.
- Filter bug-related reviews using keyword-based detection.
- Analyze review sentiments (positive, negative, neutral).
- Cluster similar game reviews using KMeans & visualize them with PCA.
- Build an interactive dashboard with Streamlit for visual exploration.

---

## Tech Stack

- **Language:** Python  
- **Data Handling:** Pandas, NumPy  
- **NLP & Sentiment Analysis:** NLTK, TextBlob  
- **ML & Clustering:** Scikit-learn (KMeans, PCA), TF-IDF  
- **Visualization:** Matplotlib, Seaborn, Plotly  
- **Deployment:** Streamlit

---

## Project Architecture

The system follows an end-to-end data pipeline from data collection to interactive visualization. Below is the architectural breakdown:

![image](https://github.com/user-attachments/assets/779c9b47-d2e5-4a88-94dc-8282862054cd)


## Project Flow

> You can replicate the project by following this sequence:

1. `Scrapper.ipynb` – Scrape reviews from Steam using AppIDs.
2. `clean_dataset.ipynb` – Clean and preprocess textual data.
3. `game_review_analysis.ipynb` – Conduct sentiment analysis and keyword filtering.
4. `steam_game_bug_analysis.ipynb` – Apply TF-IDF, clustering (KMeans), PCA visualization.
5. `eda.ipynb` – Perform exploratory data analysis.
6. `app.py` – Launch the interactive Streamlit dashboard.

> !! Note that not all dataset is uploaded to the repo, but you can scrape and filter your own data by running the project in the following order Scrapper.ipynnb -> clean_dataset.ipyn -> game review analysis.ipynb to check if the code is working or not -> steam game bug analysis.ipynb -> eda.ipynb -> app.py

---

## Key Features

- **Bug Detection:** Filters reviews containing keywords like _"bug"_, _"crash"_, _"error"_, _"lag"_.
- **Sentiment Classification:** Labels user sentiment using polarity scores from TextBlob.
- **Unsupervised Clustering:** KMeans used for discovering natural groupings among reviews.
- **PCA Visualization:** Clusters projected into 2D for better visual understanding.
- **Interactive Dashboard:** Streamlit app allows users to dynamically explore findings.

---

## 📈 Sample Visuals

- Sentiment polarity distribution graphs
- Clustering scatter plots (PCA-reduced)
- Word clouds for frequent bug terms
- Bar charts for game vs bug count

---

## Skills Demonstrated

- Data collection via web scraping  
- Regex-based text preprocessing  
- NLP pipeline implementation  
- Model interpretation & EDA  
- Real-world problem-solving with unstructured data  
- UI/UX design with dashboards

---

## Learnings

- Applied real-world NLP techniques to messy review data  
- Learned how to deploy end-to-end data science solutions  
- Improved Python proficiency and analytical thinking  
- Gained insights into how user feedback can guide product improvement

---

## Future Enhancements

- Deploy dashboard as a web app with Docker/Heroku
- Introduce advanced sentiment models like VADER or transformers
- Link bug trends with game ratings and player count
- Support multilingual review analysis

---

For questions or suggestions, feel free to raise an issue or contribute.





