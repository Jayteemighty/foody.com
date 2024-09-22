from pydantic import BaseModel, EmailStr
from typing import List
from bson import ObjectId

class User(BaseModel):
    id: ObjectId
    name: str
    email: EmailStr
    username: str
    password_hash: str
    is_verified: bool = False

class Conversation(BaseModel):
    user_id: ObjectId
    questions: List[str]
    answers: List[str]
