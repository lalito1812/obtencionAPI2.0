from fastapi import FastAPI

app = FastAPI()

dogs_data = {
    "labrador": {"origin": "Canada", "size": "Large", "lifespan": "10-12 years"},
    "pug": {"origin": "China", "size": "Small", "lifespan": "12-15 years"},
    "german_shepherd": {"origin": "Germany", "size": "Large", "lifespan": "9-13 years"},
}

@app.get("/")
def home():
    return {
        "message": "Welcome to the Public Dog API!",
        "available_breeds": list(dogs_data.keys()),
        "breeds_info": dogs_data
    }


@app.get("/breeds/")
def get_breeds():
    return {"available_breeds": list(dogs_data.keys())}

@app.get("/breeds/{breed_name}")
def get_breed_info(breed_name: str):
    breed = dogs_data.get(breed_name.lower())
    if breed:
        return breed
    return {"error": "Breed not found"}
