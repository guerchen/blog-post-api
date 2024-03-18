import pymongo
from datetime import date
import os

from fastapi import FastAPI, status, Header, HTTPException
from pydantic import BaseModel
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.mongo_setup import db

load_dotenv()
api_key=os.getenv("API_SECRET_KEY")

app = FastAPI()

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

class Post(BaseModel):
    title: str
    date: date
    content: str

@app.get("/posts")
def read_all():
    posts = list(db.blog_posts.find().sort("date", pymongo.DESCENDING))

    for post in posts:
        post["id"] = str(post["_id"])
        del post["_id"]

    return {"posts": posts}

@app.get("/posts/{item_id}")
def read_item(item_id: str):
    try:
        query = db.blog_posts.find_one({"_id" :ObjectId(item_id)})

        id = str(query["_id"])
        del query["_id"]

        return {"id": id, "data": query}
    
    except:
        raise HTTPException(status_code=404, detail="Not found")

@app.put("/posts/{item_id}")
def update_item(
        item_id: str, post: Post, authorization: str = Header(default=None)
    ):
    if authorization != api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    try:
        db.blog_posts.update_one(
            {"_id": ObjectId(item_id)},
            {
                "$set": jsonable_encoder(post)
            }
        )

        return {"updated": True}
    
    except:
        raise HTTPException(status_code=404, detail="Not found")

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_item(post: Post, authorization: str = Header(default=None)):
    if authorization != api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    post = jsonable_encoder(post)
    id = str(db.blog_posts.insert_one(post).inserted_id)

    return {"created":True,"id": id}

@app.delete("/posts/{item_id}")
def delete_item(item_id: str, authorization: str = Header(default=None)):
    if authorization != api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    try:
        db.blog_posts.delete_one({"_id":ObjectId(item_id)})
        return {"deleted":True}
    
    except:
        raise HTTPException(status_code=404, detail="Not found")
