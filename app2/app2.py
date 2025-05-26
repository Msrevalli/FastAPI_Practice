from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

# Base model for user input (no id needed from client)
class UserIn(BaseModel):
    name: str
    age: Optional[int] = None

# Full user model (id included)
class User(UserIn):
    id: UUID

# Partial update model for PATCH
class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

# In-memory storage
users_db: List[User] = []

# Create user (POST) - body param
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    new_user = User(id=uuid4(), **user.dict())
    users_db.append(new_user)
    return new_user

# Get all users (GET)
@app.get("/users/", response_model=List[User])
async def get_all_users():
    return users_db

# Get a user by ID (GET)
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: UUID):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Replace a user (PUT) - full body
@app.put("/users/{user_id}", response_model=User)
async def replace_user(user_id: UUID, user_data: UserIn):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            updated_user = User(id=user_id, **user_data.dict())
            users_db[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Partially update a user (PATCH) - partial body
@app.patch("/users/{user_id}", response_model=User)
async def update_user(user_id: UUID, user_update: UserUpdate):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            user_dict = user.dict()
            update_fields = user_update.dict(exclude_unset=True)
            user_dict.update(update_fields)
            updated_user = User(**user_dict)
            users_db[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Delete a user (DELETE)
@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(idx)
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
