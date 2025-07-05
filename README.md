# Movie Recommender System

A modern Streamlit web app that recommends movies based on your selection using content-based filtering.

live :-https://ai-movie-suggester.streamlit.app/

## Features
- Select a movie and get 5 similar recommendations
- Clean, modern UI/UX
- Easy to run locally

## Setup
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Files
- `app.py` - Main Streamlit app
- `movies.pkl` - Movie data (pandas DataFrame)
- `similarity.pkl` - Similarity matrix

## Requirements
- Python 3.7+
- See `requirements.txt`

## License
This project is licensed under the MIT License. 
