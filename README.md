# 🎬 Movie Recommendation System

This project is a *content-based movie recommendation system* created using *Python, **pandas, **scikit-learn, and **Streamlit*.  
It recommends up to *500 similar movies* based on the *cast and crew* of a given movie title.

---

## 🚀 Features

- Uses *TF-IDF Vectorization* and *Cosine Similarity* for similarity computation.  
- Provides up to *500 similar movies* for any movie entered.  
- Built with a clean and interactive *Streamlit web interface*.  
- Supports large movie datasets in .csv or .zip format.  

---

## 🧠 How It Works

1. Loads the dataset (movies1.csv.zip) containing movie information.  
2. Combines the cast and crew columns to form a unified textual feature.  
3. Uses *TF-IDF Vectorizer* to convert text data into numerical vectors.  
4. Calculates *cosine similarity* among all movies.  
5. When a user enters a movie name, it finds and displays the top 500 similar ones.  

---

## 🗂 Dataset Format

The dataset must include at least the following columns:

| Column | Description |
|:-------|:-------------|
| title | Movie title |
| cast | Main actors/actresses |
| crew | Crew members (e.g., directors, producers) |

*Example:*

| title | cast | crew |
|:------|:------|:------|
| Inception | Leonardo DiCaprio, Joseph Gordon-Levitt | Christopher Nolan, Emma Thomas |

---

## 🧰 Requirements

Install the necessary dependencies using pip:

bash
pip install pandas scikit-learn streamlit


---

## 🏗 Project Structure


movie-recommender/
│
├── movies1.csv.zip           # Dataset file
├── app.py                    # Main Python file (this code)
└── README.md                 # Project documentation


---

## ▶ How to Run the App

1. Place your dataset file (movies1.csv.zip) in the same folder as app.py.  
2. Open your terminal or command prompt in that folder.  
3. Run the Streamlit app:

   bash
   streamlit run app.py
   

4. The app will open automatically in your browser (default: http://localhost:8501).

---

## 🖥 Usage Instructions

1. Enter a movie name in the text box (e.g., Inception).  
2. Click the *"Recommend"* button.  
3. The system will display a list of up to *500 similar movies*.

---

## ⚙ Code Explanation

### Main Steps in the Code:

- *Data Preparation:* Selects title, cast, and crew columns and merges them into one.  
- *Feature Extraction:* Converts text data into vectors using TF-IDF.  
- *Similarity Calculation:* Computes pairwise cosine similarity between movies.  
- *Recommendation Logic:* Sorts and retrieves the most similar 500 movies.

### Example Function:

python
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


---

## 🧩 Example Output

If you enter:


Inception


You may see results like:


1. Interstellar  
2. The Dark Knight  
3. The Prestige  
4. Memento  
5. Tenet  
... up to 500 results


---

## 📄 License

This project is licensed under the *MIT License*. You are free to use, modify, and share it.

---

## ❤ Acknowledgements

- [Streamlit](https://streamlit.io) — for the web interface.  
- [scikit-learn](https://scikit-learn.org) — for machine learning tools.  
- [The Movie Database (TMDB)](https://www.themoviedb.org/) — for movie data sources.

---

*Developed with ❤ using Python and Streamlit.*
