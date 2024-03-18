import pymongo
import os

from dotenv import load_dotenv

load_dotenv()
mongo_conn_string=os.getenv("MONGO_CONN_STRING")

client = pymongo.MongoClient(mongo_conn_string)
db = client.myblog