from pydantic import BaseModel


class Model(BaseModel):
    model:str="llama-3.1-8b-instant"
    user_input:str
    api_key:str=None

