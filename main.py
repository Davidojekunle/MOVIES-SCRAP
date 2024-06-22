from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from intapi import router
from kdramaapi import route

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

def internationals():
    app.include_router(router)

def kdrama():
    app.include_router(route)

kdrama() 