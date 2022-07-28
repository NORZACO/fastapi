from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from models.mymodels import UserUpdateRequest

from models.mymodels import User, Gender, Roles


app = FastAPI()



databases : List[User] = [
    User(
        #id=uuid4(),
         id = UUID("fe37e66b-632b-47f8-9aa8-a13eb90e7c3a"),
         First_name="Katempa",
         Last_name="Bondo",
         Middle_name = "Victirine",
         age = 14,
         gender=Gender.female,
         roles=[Roles.student]
        ),
    
    User(#id=uuid4(),
         id= UUID("c936f584-e1e0-4d7b-93e9-99b16e28908c"),
         First_name = "Etienne",
         Last_name  = "Shadrick",
         Middle_name = "Kyamata",
          
         age = 10,
         gender=Gender.male,
         roles=[Roles.admin, Roles.user]
        )
]


@app.get('/api/v1/users')
async def fetch_users():
    context = { 'databases' : databases}
    return context


@app.post('/api/v1/users')
async def usersregister_user(user : User):
    databases.append(user)
    context = {'user' : user }
    #context = {user }
    return context

url = "http://127.0.0.1:8000/api/v1/users"

@app.delete('/api/v1/users/{user_id}')
async def deling_user(user_id : UUID):
    for user in databases:
        if user.id == user_id:
            databases.remove(user)
            return
    raise HTTPException(
        status_code = 404, 
        detail = f"User with id: {user_id} does not exists"
    )



@app.put("api/v1/users{user_id}")
async def Update_user(user_update : UserUpdateRequest, user_id : UUID):
    
    # CHECK IF THE USER IS IN DATABASES
    for user in databases:
        
        if user.id == user_id:
            # UPDATE FIRST NAME
            if user_update.Fisrt_name is not None:
                user.First_name = user_update.Fisrt_name
                
            # UPDATE LAST NAME
            if user_update.Last_name is not None:
                user.Last_name = user_update.Last_name
                
            # UPDATE MIDDLE NAME  
            if user_update.Middle_name is not None:
                user.Middle_name = user_update.Middle_name
                
            # UPDATE AGE NAME
            #if user_update.age is not None:
            #    user.age = user_update.age
            
            # UPDATE FIRST NAME
            if user_update.roles is not None:
                user.roles = user_update.roles  
            return
    # RAISE THE ERROR=
    raise HTTPException(
        status_code=404,
        detail= f"User with this id: {user_id} does not exists"
        )
                
    
























items = {"foo": "The Foo Wrestlers"}
@app.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404, 
            detail= f"items with thi Item : {item_id} not found"
            )
    return {"item": items[item_id]}