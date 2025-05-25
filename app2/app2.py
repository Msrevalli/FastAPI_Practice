from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class UserSchema(BaseModel):
    name: str
    no: int

users = []  # In-memory storage

@app.post("/createuser/")
def create_user(user: UserSchema):
    # Check for duplicates
    for u in users:
        if u["no"] == user.no:
            raise HTTPException(status_code=400, detail="User with this number already exists")
    users.append(user.dict())
    return {"message": "New user added successfully"}

@app.get("/allusers/", response_model=List[UserSchema])
def all_users():
    return users

@app.put("/updateuser/{user_no}")
def update_user(user_no: int, updated_user: UserSchema):
    for index, user in enumerate(users):
        if user["no"] == user_no:
            users[index] = updated_user.dict()
            return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/deleteuser/{user_no}")
def delete_user(user_no: int):
    for index, user in enumerate(users):
        if user["no"] == user_no:
            users.pop(index)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
