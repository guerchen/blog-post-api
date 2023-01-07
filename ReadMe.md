# Personal website's blog API

First of all, the objective of this project was learning how to create simple CRUD APIs using FastAPI. Secondly, I wished to be able to edit and create blog posts in my website without having to redeploy every single time.

## How to run

Prerrequisite: Be sure to have python installed on your machine and clone this repository
1. To install libraries, run on the terminal at the folder you've saved this repo:
```
py -m pip install -r requirements.txt
```
2. Create a MongoDB database and place your credentials in mongo_setup.py
3. Then, run this command to start the API server locally:
```
uvicorn app.main:app --reload
```

## How to run (option 2)

You can also use the dockerfile to run this repo. To do this, just execute:
```
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage
```

Yay! This must work! If it doesn't, get in touch! We can troubleshoot together. 