import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# STEP 1: Load the movie data
data = pd.read_csv(r"C:\Users\Divya P\Downloads\movies1.csv.zip")

# STEP 2: Combine useful text columns
data = data[['title', 'cast', 'crew']].dropna()
data['combined'] = data['cast'].astype(str) + ' ' + data['crew'].astype(str)

# STEP 3: Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english', max_features=10000)
tfidf_matrix = tfidf.fit_transform(data['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# STEP 4: Define recommendation function
def recommend(title):
    title_lower = title.lower()
    titles_lower = data['title'].str.lower().tolist()
    if title_lower not in titles_lower:
        return ["Movie not found! Please check the title."]
    idx = titles_lower.index(title_lower)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:501]]
    return data['title'].iloc[movie_indices].tolist()

# STEP 5: Streamlit app
st.title("🎬 Movie Recommendation System")
movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_name.strip():
        recommendations = recommend(movie_name)
        st.write(f"### Top 500 movies similar to '{movie_name}':")
        for i, rec in enumerate(recommendations, start=1):
            st.write(f"{i}. {rec}")
    else:
        st.warning("Please enter a movie name.")