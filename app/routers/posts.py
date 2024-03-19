import pymongo
import os

from fastapi import APIRouter, status, Header, HTTPException
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from dotenv import load_dotenv

from app.mongo_setup import db
from app.models import Post

load_dotenv()
api_key=os.getenv("API_SECRET_KEY")


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

@router.get("")
def read_all():
    posts = list(db.blog_posts.find().sort("date", pymongo.DESCENDING))

    for post in posts:
        post["id"] = str(post["_id"])
        del post["_id"]

    return {"posts": posts}


@router.get("/{item_id}")
def read_item(item_id: str):
    try:
        query = db.blog_posts.find_one({"_id" :ObjectId(item_id)})

        id = str(query["_id"])
        del query["_id"]

        return {"id": id, "data": query}
    
    except:
        raise HTTPException(status_code=404, detail="Not found")


@router.put("/{item_id}")
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


@router.post("", status_code=status.HTTP_201_CREATED)
def create_item(post: Post, authorization: str = Header(default=None)):
    if authorization != api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    post = jsonable_encoder(post)
    id = str(db.blog_posts.insert_one(post).inserted_id)

    return {"created":True,"id": id}


@router.delete("/{item_id}")
def delete_item(item_id: str, authorization: str = Header(default=None)):
    if authorization != api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    try:
        db.blog_posts.delete_one({"_id":ObjectId(item_id)})
        return {"deleted":True}
    
    except:
        raise HTTPException(status_code=404, detail="Not found")