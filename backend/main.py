from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chains import generate_response
from model import Model
import json
import os
from chains import store


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('url','*')],  
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
async def index():
    return "API"

@app.post("/chat")
async def home(model:Model):
    try:
        #print(model)
        if model.api_key=='None':
            model.api_key=None
        response =  generate_response(model.user_input,model.model,model.api_key)
        print(store,'wfwrgf')
    except Exception as e:
        #print(e)
        return json.dumps({"error":"Error"})
    return response

@app.post("/refresh")
async def refresh():
    store.clear()