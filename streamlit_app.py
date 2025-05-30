import pickle
import streamlit as st
import pandas as pd
import requests

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

import urllib.parse

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=<your_api_key>&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        print("Error fetching poster:", e)
    return "https://via.placeholder.com/200x300.png?text=No+Image"


# Recommend movies function
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return []

    movie_index = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movie_list:
        index = i[0]
        recommendations.append({
            'title': movies.iloc[index].title,
            'poster': fetch_poster(movies.iloc[index].movie_id),
            'tags': movies.iloc[index].tags[:150] + '...'
        })
    return recommendations

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")
st.markdown("#### Enter a movie you like and get similar movie suggestions!")

# Global styling
st.markdown("""
    <style>
    .stApp {
        background-color: black;
    }

    h1, h2, h3, h4, h5, h6 {
        color: red !important;
    }

        .movie-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: start;
        align-items: flex-start;
    }
    
    .movie-card {
        background-color: #e0e0e0;
        padding: 15px;
        border-radius: 12px;
        width: 200px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        color: black;
        flex-shrink: 0;
    }
    
    .movie-card img {
        width: 100%;
        height: auto;
        object-fit: cover;
        border-radius: 10px;
    }

    .movie-title {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        color: black;
    }

    .movie-tags {
        font-size: 13px;
        color: black;
        margin-top: 5px;
    }

    .movie-info {
        font-size: 13px;
        color: black;
        margin-top: 5px;
        word-wrap: break-word;
    }

    .stSelectbox > div {
        color: white !important;
    }

    .stButton button {
        background-color: red;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


movie_titles = movies['title'].sort_values().tolist()
selected_movie = st.selectbox("Search for a movie", movie_titles)

if st.button("Show Recommendations"):
    if selected_movie:
        results = recommend(selected_movie)
        if not results:
            st.error("Movie not found! Try another.")
        else:
            # Movie cards layout
            st.markdown('<div class="movie-container">', unsafe_allow_html=True)

            for movie in results:
                st.markdown(f"""
                    <div class="movie-card">
                        <img src="{movie['poster']}" alt="{movie['title']} poster">
                        <div class="movie-title">{movie['title']}</div>
                        <div class="movie-tags">{movie['tags']}</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
