# Music Recommendation System

A content-based music recommendation system built using Python, Natural Language Processing (NLP), and Streamlit. This project recommends songs similar to a user’s input by analyzing song metadata like artist, genre, album, and user ratings.

---

## 📌 Features

- Content-based filtering using song metadata (artist, genre, album, ratings)
- NLP-based tag generation and vectorization
- Cosine similarity for identifying similar songs
- Interactive web interface built with Streamlit
- Supports both Hindi and English songs

---

## 🛠 Technologies Used

- *Python*  
- *Pandas & NumPy* – Data cleaning and manipulation  
- *Scikit-learn* – CountVectorizer, cosine_similarity  
- *Streamlit* – Web interface for the recommendation system  
- *Jupyter Notebook* – Development and experimentation  
- *CSV Dataset* – Song metadata (Song-Name, Artist, Genre, Album, Rating)

---

## ⚙ How It Works

1. *Data Preprocessing*  
   - Remove missing values and duplicates  
   - Clean and standardize text data  
   - Create a combined tags column using key metadata  

2. *Vectorization*  
   - Convert tags into numerical vectors using CountVectorizer  
   - Transform text data into feature vectors for similarity comparison  

3. *Similarity Calculation*  
   - Use cosine similarity to calculate how similar songs are to one another  
   - Generate a similarity matrix for all songs  

4. *Recommendation*  
   - User inputs a song title  
   - The system retrieves similar songs based on the cosine similarity scores  
   - Displays the top 5 most similar songs  

5. *Deployment*  
   - Built with Streamlit for an easy-to-use web interface
