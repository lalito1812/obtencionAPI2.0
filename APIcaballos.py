from fastapi import FastAPI

app = FastAPI()

horses_data = {
    "arabian": {"origin": "Arabia", "size": "Medium", "lifespan": "25-30 years"},
    "andalusian": {"origin": "Spain", "size": "Large", "lifespan": "20-25 years"},
    "thoroughbred": {"origin": "United Kingdom", "size": "Large", "lifespan": "25-30 years"},
}

@app.get("/")
def home():
    return {"message": "Welcome to the Public Horse API!"}

@app.get("/breeds/")
def get_breeds():
    return {"available_breeds": list(horses_data.keys())}

@app.get("/breeds/{breed_name}")
def get_breed_info(breed_name: str):
    breed = horses_data.get(breed_name.lower())
    if breed:
        return breed
    return {"error": "Breed not found"}
