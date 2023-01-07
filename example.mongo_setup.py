import pymongo

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@ariels-blog.ioq5i5c.mongodb.net/?retryWrites=true&w=majority")
db = client.myblog

api_key = 'jwt'