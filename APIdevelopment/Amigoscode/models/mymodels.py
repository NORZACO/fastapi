
from mimetypes import init
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum



class Gender(str, Enum):
    male = "male"
    female = "female"


class Roles(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
    teacher = "teacher"
    cleaner = "cleaner"
    vikaret = "vikaret"
    
    
class User(BaseModel):
    id : Optional[UUID] = uuid4()
    First_name : str
    Last_name : str
    Middle_name : Optional[str]
    gender : Gender
    roles : List[Roles]
    
    
class UserUpdateRequest(BaseModel):
    Fisrt_name : Optional[str]
    Last_name : Optional[str]     
    Middle_name : Optional[str]
    roles : Optional[List[Roles]]

    
    