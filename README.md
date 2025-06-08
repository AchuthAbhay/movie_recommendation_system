# Movie Recommender System

A content-based movie recommendation system built using Python and Streamlit. It leverages Natural Language Processing (NLP) techniques and cosine similarity to recommend movies based on user selection.

---

## Overview

This project uses two cleaned datasets from the [TMDb 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) available on Kaggle. After extensive data cleaning and text preprocessing, the system recommends similar movies by analyzing movie metadata.

---

## Features

- Cleaned and preprocessed raw TMDb datasets:
  - Text normalization including lowercasing, lemmatization, and stopwords removal.
  - Tokenization and vectorization of movie metadata for similarity computation.

- Used **Cosine Similarity** to measure similarity between movie features in a high-dimensional vector space, which provides effective recommendations.

- Interactive **Streamlit** app interface for easy movie selection and recommendation display with posters.

- Dynamic poster fetching using TMDb API for visually rich recommendations.

---

## Methodology

1. **Data Cleaning & Preprocessing:**  
   - Merged two TMDb datasets.  
   - Removed irrelevant columns and handled missing data.  
   - Applied text preprocessing: stopword removal, lemmatization, and tokenization.

2. **Vectorization:**  
   - Converted textual metadata into numerical vectors using TF-IDF or Count Vectorizer.

3. **Similarity Calculation:**  
   - Computed cosine similarity between movie vectors to find the closest movies.

4. **Recommendation System:**  
   - For a selected movie, finds top 5 most similar movies using cosine similarity.

5. **Poster Retrieval:**  
   - Fetches movie posters dynamically via TMDb API for an enhanced user experience.

---

## Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn (for vectorization & similarity computation)  
- NLTK (for text preprocessing and lemmatization)  
- Requests (for API calls)  
- Streamlit (for the web interface)  

---
## User Interface Preview

![image](https://github.com/user-attachments/assets/9485fcd8-cea4-466e-8e91-790db74bdd12)



## Note on Large Data File
  Due to size constraints, the similarity.pkl file is not included in this repo. The app automatically downloads this file from a Google Drive link on first run.

## Live Demo

Check out the deployed Movie Recommendation App here:  
[https://huggingface.co/spaces/Synaptra/movie-recommender-Achuthabhay](https://huggingface.co/spaces/Synaptra/movie-recommender-Achuthabhay)

  

## Setup & Usage

1. Clone this repo:  
   ```bash
   git clone https://github.com/AchuthAbhay/movie_recommendation_system.git
   cd movie_recommendation_system
2.Install dependencies and run app:  
  ```bash
    pip install -r requirements.txt
    streamlit run app.py

