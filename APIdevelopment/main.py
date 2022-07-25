
from fastapi import FastAPI

app = FastAPI()

#PASS APERATION OR ROUTER
@app.get("/login")
async def login_user():
    context = {'message' : 'hellow world'}
    return context

class Position():
    def __init__(self, manager, vakter, CEO):
        self.manager = manager
        self.vakter = vakter
        self.CEO = CEO
        


class Living():
    pass



class Student(Position):
    def __init__(self, first_name, last_name, klasse, age, country, manager, vakter, CEO):
        super().__init__(manager, vakter, CEO)
        self.first_name = first_name
        self.last_name = last_name
        self.klasse = klasse
        self.age = age
        self.country = country
        

    def get_username(self):
        context  = {
            'firstname' : self.first_name,
            'lastname': self.last_name
        }
        return context

    def get_full_name(self):
        return self.first_name.title() + " " + self.last_name.title()
    

    def get_successfull_message(self, message):
        self.message = message.title()
        return self.message


    def get_name_with_age(self, name: str, age: int):
        self.name = name
        self.age = age
        return self.name + " is this old: " + self.age
        






b1 = Student('mwamuzi', 'shada', '3aad',24, 'country', "ElonMaks", "Toalett Vakter", "CEO")


b1.get_username()

@app.get("/posts")
async def get_posts():
    data = {
        'data' : b1.get_username(),
        'age' : b1.age
    }
    return data


@app.get("/items/{item_id}")
async def raed_item_id(item_id : int):
    context = {
        'item_id' : item_id
    }
    return context

#b2 = Student("Katempa", "Bomdo", "3 Klasse", 13, "Norge")

#b3 = Student("Mwamuzi", "Shadrick", "3DD", 24, "NORGE")

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


@app.post("/createpost")
def get_full_name():
    context = {
        'names' : b1.get_full_name()
    }
    return context





from enum import Enum




class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
