from fastapi import FastAPI
from app import planetapi

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hz/")
def read_hz(radius: float, effective_temp: float):
    return planetapi.habitable_zones(radius, effective_temp)


@app.get("/random-star")
def read_random_star():
    star = planetapi.random_star()
    print(star)
    return star


@app.get("/similar_exoplanets/")
def read_similar_exoplanets(distance_to_star, planet_radius, tilt):
    return 1
