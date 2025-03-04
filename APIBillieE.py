from fastapi import FastAPI

app = FastAPI()

billie_data = {
    "name": "Billie Eilish",
    "birthdate": "2001-12-18",
    "birthplace": "Los Angeles, California, USA",
    "genre": ["Pop", "Alternative", "Indie", "Electropop"],
    "debut_album": "When We All Fall Asleep, Where Do We Go?",
    "hit_songs": ["Bad Guy", "Bury a Friend", "Everything I Wanted", "No Time to Die"],
    "awards": ["5 Grammy Awards", "2 American Music Awards", "3 MTV Video Music Awards"],
}

@app.get("/")
def home():
    return {"message": "Welcome to the Billie Eilish API!"}

@app.get("/biography/")
def get_biography():
    return {
        "name": billie_data["name"],
        "birthdate": billie_data["birthdate"],
        "birthplace": billie_data["birthplace"],
        "genre": billie_data["genre"]
    }

@app.get("/album/")
def get_debut_album():
    return {"debut_album": billie_data["debut_album"]}

@app.get("/hit_songs/")
def get_hit_songs():
    return {"hit_songs": billie_data["hit_songs"]}

@app.get("/awards/")
def get_awards():
    return {"awards": billie_data["awards"]}
