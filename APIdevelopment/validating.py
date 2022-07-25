
from .main import *
from pydantic import BaseModel

class Post(BaseModel):
    Title : str
    Content : str
    Name = str
    Age = int
    Saldo = float
 
new_posting_message = b1.get_successfull_message("We are creating the new post from BaseModel pydantic")   
    
@portfolio.post("/creatingpost")
def post_creating_aSuccessfull_message(new_user : Post):
    print(new_user)
   # context = {
   #     #'new_posting_message' : new_posting_message,
   #     'Title' : f"Title {new_user['Title']}", 
   #     'Content' : f"Content {new_user['Content']}", 
   #     'User' : f"User: {new_user['Name']}",
   #     'Age' : f"Age : {new_user['Age']}",
   #     'Saldo' : f"Saldo : {new_user['Saldo']}"
   # }
    context = {"data" : "New Post"}
    return context