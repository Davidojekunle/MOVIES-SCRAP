from fastapi import APIRouter
from kdrama.sessions import get_all_movies, add_movie, search_movies, get_trending_movies
from fastapi import HTTPException
from kdrama.schemas import kdrama


route = APIRouter()

@route.get("/all")
def all_movies():
    movies =  get_all_movies()
    if not movies:
        return HTTPException(status_code=404, message= 'No movies')
    return movies

@route.post('/add-movie')
async def addmovie(kdrama : kdrama):
    kdrama = await add_movie(kdrama.name, kdrama.date, kdrama.description, kdrama.image_link, kdrama.url)
    if not kdrama:
        return HTTPException(status_code=404, message="Movie not added successfully") 
    else:
        return kdrama

@route.get("/search")
def search(q: str):
    movies = search_movies(q)
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found")
    return movies

@route.get("/trending")
def trending_movies():
    movies = get_trending_movies()
    if not movies:
        raise HTTPException(status_code=404, detail="No trending movies found")
    return movies