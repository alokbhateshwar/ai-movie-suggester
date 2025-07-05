import pickle
import streamlit as st
import requests
import pandas as pd

# TMDB API Key
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# Function to fetch poster
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except Exception as e:
        print(f"Error fetching poster for ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

# Recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_names = []
    for i in distances:
        title = movies.iloc[i[0]].title
        recommended_names.append(title)
    return recommended_names

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(135deg, #e0e7ff 0%, #f0f4ff 100%) !important;
    }
    .main-title {
        font-size: 2.7rem;
        font-weight: bold;
        color: #3b82f6;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #555;
        text-align: center;
        margin-bottom: 2.2rem;
    }
    .rec-title {
        font-size: 1.3rem;
        color: #222;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    .movie-box {
        background: #fff;
        border-radius: 14px;
        padding: 1.1rem 1.7rem;
        margin-bottom: 1.1rem;
        box-shadow: 0 4px 18px rgba(59,130,246,0.10);
        font-size: 1.13rem;
        font-weight: 500;
        color: #222;
        transition: transform 0.15s, box-shadow 0.15s;
        text-align: center;
        border: 1.5px solid #e0e7ff;
    }
    .movie-box:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0 8px 32px rgba(59,130,246,0.18);
        border: 1.5px solid #3b82f6;
        background: #f0f7ff;
    }
    .stButton > button {
        background: linear-gradient(90deg, #3b82f6 0%, #60a5fa 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 2.2rem;
        border: none;
        margin: 0 auto;
        display: block;
        font-size: 1.1rem;
        box-shadow: 0 2px 8px rgba(59,130,246,0.10);
        transition: background 0.2s, box-shadow 0.2s;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #2563eb 0%, #60a5fa 100%);
        box-shadow: 0 4px 16px rgba(59,130,246,0.18);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get personalized movie recommendations instantly. Select a movie you like and discover your next favorite!</div>', unsafe_allow_html=True)

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))        # DataFrame with 'title' and 'movie_id'
similarity = pickle.load(open('similarity.pkl', 'rb'))  # 2D NumPy array

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie you like:", movie_list)

if st.button("Show Recommendations"):
    with st.spinner('🔍 Finding similar movies...'):
        names = recommend(selected_movie)
    st.markdown('<div class="rec-title">Top 5 Recommendations:</div>', unsafe_allow_html=True)
    for name in names:
        st.markdown(f'<div class="movie-box">{name}</div>', unsafe_allow_html=True)

st.markdown(
    '<div style="text-align:center; color: #888; font-size: 0.95rem; margin-top: 2.5rem;">'
    'Made by <b>Alok Bhateshwar</b>'
    '</div>',
    unsafe_allow_html=True
)
