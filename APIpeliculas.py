from fastapi import FastAPI

app = FastAPI()

movies_data = {
    "inception": {
        "title": "Inception",
        "director": "Christopher Nolan",
        "release_year": 2010,
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "rating": 8.8
    },
    "the_dark_knight": {
        "title": "The Dark Knight",
        "director": "Christopher Nolan",
        "release_year": 2008,
        "genres": ["Action", "Crime", "Drama"],
        "rating": 9.0
    },
    "interstellar": {
        "title": "Interstellar",
        "director": "Christopher Nolan",
        "release_year": 2014,
        "genres": ["Adventure", "Drama", "Sci-Fi"],
        "rating": 8.6
    },
    "parasite": {
        "title": "Parasite",
        "director": "Bong Joon-ho",
        "release_year": 2019,
        "genres": ["Comedy", "Drama", "Thriller"],
        "rating": 8.6
    },
}

@app.get("/")
def home():
    return {"message": "Welcome to the Public Movies API!"}

@app.get("/movies/")
def get_movies():
    return {"available_movies": list(movies_data.keys())}

@app.get("/movies/{movie_id}")
def get_movie_info(movie_id: str):
    movie = movies_data.get(movie_id.lower())
    if movie:
        return movie
    return {"error": "Movie not found"}
