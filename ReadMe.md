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
uvicorn main:app --reload
```

Yay! This must work! If it doens't, get in touch! We can troubleshoot together. 