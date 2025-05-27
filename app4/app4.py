from fastapi import FastAPI, HTTPException, Header
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

class UserListResponse(BaseModel):
    request_id: str
    users: List[User]

# Partial update model for PATCH
class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

# In-memory storage
users_db: List[User] = []

# Example: Add X-API-Key header to user creation
@app.post("/users/", response_model=User)
async def create_user(user: UserIn, x_api_key: Optional[str] = Header(default=None)):
    print(f"Received X-API-Key: {x_api_key}")  # Logging header
    new_user = User(id=uuid4(), **user.dict())
    users_db.append(new_user)
    return new_user

# Example: Add X-Request-Id header to fetch all users
@app.get("/users/", response_model=UserListResponse)
async def get_all_users(x_request_id: Optional[str] = Header(default=None)):
    return {
        "request_id": x_request_id,
        "users": users_db
    }

# Example: Custom header in PATCH
@app.patch("/users/{user_id}", response_model=User)
async def update_user(
    user_id: UUID,
    user_update: UserUpdate,
    x_user_role: Optional[str] = Header(default="user")
):
    if x_user_role != "admin":
        raise HTTPException(status_code=403, detail="Insufficient role to patch user")
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            user_dict = user.dict()
            update_fields = user_update.dict(exclude_unset=True)
            user_dict.update(update_fields)
            updated_user = User(**user_dict)
            users_db[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")
