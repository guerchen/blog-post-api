from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import posts, visits

app = FastAPI(title="Blog Post API")
app.include_router(posts.router)
app.include_router(visits.router)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://guerchenzon.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
