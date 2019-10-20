from fastapi import FastAPI
from app import planetapi

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hz")
def read_hz(radius: float, effective_temp: float):
    return planetapi.habitable_zones(radius, effective_temp)


@app.get("/stats/stars")
def stats_stars():
    return planetapi.get_star_stats()


@app.get("/stats/planets")
def stats_planets(fields: str = None):
    if fields:
        fields = fields.split(',')
    return planetapi.get_planet_stats(fields)


@app.get("/random-star")
def read_random_star():
    star = planetapi.random_star()
    return star


@app.get("/similar_exoplanets")
def read_similar_exoplanets(pl_rade: float = 1, pl_masse: float = 1, pl_distance: float = 1):
    return planetapi.similar_planets(pl_rade, pl_masse, pl_distance)
