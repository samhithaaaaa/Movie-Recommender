🎬 Movie Recommender System

A content-based Movie Recommender System built using Python and Streamlit. Enter a movie you like and get recommendations for similar movies, along with posters and genre tags!

🔍 Features

- Search and select a movie title
- Get top 5 similar movie recommendations
- Display posters, genres/tags, and movie titles
- Styled with custom CSS for a card-based layout
- Integrated with TMDb API to fetch real movie posters


📁 Project Structure

├── streamlit_app.py # Main Streamlit app

├── movies_list.pkl # Pickled file containing movie data (title, tags, movie_id)

├── similarity.pkl # Precomputed similarity matrix

├── requirements.txt # Python dependencies

└── README.md # Project documentation


🧠 How It Works

Data: Movies data is preprocessed and saved in movies_list.pkl, containing features like title, tags, and TMDb movie_id.
Similarity: A cosine similarity matrix is calculated using TF-IDF or count vectorization and stored in similarity.pkl.
Recommendation Logic: Given a movie title, the app finds the most similar movies based on tags and returns their posters via the TMDb API.
🔑 API Key

This project uses TMDb API to fetch poster images.

Replace the hardcoded API key in streamlit_app.py with your own:
api_key = "your_api_key_here"


🛠️ Technologies Used

Python
Streamlit
Pandas
Requests
Pickle
TMDb API




