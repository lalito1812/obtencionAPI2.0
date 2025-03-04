from fastapi import FastAPI

app = FastAPI()

cats_data = {
    "persian": {"origin": "Iran", "size": "Medium to Large", "lifespan": "12-17 years"},
    "siamese": {"origin": "Thailand", "size": "Medium", "lifespan": "15-20 years"},
    "maine_coon": {"origin": "United States", "size": "Large", "lifespan": "12-15 years"},
}

@app.get("/")
def home():
    return {"message": "Welcome to the Public Cat API!"}

@app.get("/breeds/")
def get_breeds():
    return {"available_breeds": list(cats_data.keys())}

@app.get("/breeds/{breed_name}")
def get_breed_info(breed_name: str):
    breed = cats_data.get(breed_name.lower())
    if breed:
        return breed
    return {"error": "Breed not found"}
