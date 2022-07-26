
from main import *
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


portfolio = FastAPI()


class Post(BaseModel):
    Title : str
    Content : str
    Name = str
    Age = int
    Saldo = float
       
new_posting_message = b1.get_successfull_message("We are creating the new post from BaseModel pydantic")    
@portfolio.post("/creatposts")
def post_creating_Successfull_message(new_user : Post):
    print(new_user)
    context = {"data" : "New Post"}
    return context