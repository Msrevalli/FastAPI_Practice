## 📘 Overview

This is a **simple CRUD API** for managing users using FastAPI. It supports:

* **Create** user
* **Read** all users
* **Update** user by number
* **Delete** user by number

The app uses **in-memory storage** (`users` list), so all data is lost when the server restarts.

---

## 📦 Imports

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
```

* `FastAPI`: Used to create the API app.
* `HTTPException`: Used to return proper HTTP error codes.
* `BaseModel`: Used to define the data schema for request/response validation.
* `List`: Used for typing a list of `UserSchema` in response.

---

## 🚀 App Setup

```python
app = FastAPI()
```

Initializes the FastAPI app.

---

## 🧾 User Schema

```python
class UserSchema(BaseModel):
    name: str
    no: int
```

Defines what a **user** looks like:

* `name`: User's name (string)
* `no`: A unique number (integer)

---

## 📚 In-Memory Storage

```python
users = []
```

Stores all users in a Python list. This is **temporary** storage and **not persistent**.

---

## 🔨 Endpoints

### ✅ Create User

```python
@app.post("/createuser/")
def create_user(user: UserSchema):
    for u in users:
        if u["no"] == user.no:
            raise HTTPException(status_code=400, detail="User with this number already exists")
    users.append(user.dict())
    return {"message": "New user added successfully"}
```

* Accepts a `UserSchema` object from the client.
* Checks if a user with the same `no` already exists.
* If not, adds the user.
* Returns a success message.

### 📋 Get All Users

```python
@app.get("/allusers/", response_model=List[UserSchema])
def all_users():
    return users
```

* Returns the entire list of users.
* Uses `response_model=List[UserSchema]` to validate and format the response.

### 🔁 Update User

```python
@app.put("/updateuser/{user_no}")
def update_user(user_no: int, updated_user: UserSchema):
    for index, user in enumerate(users):
        if user["no"] == user_no:
            users[index] = updated_user.dict()
            return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")
```

* Searches for a user by `user_no` in the path.
* If found, updates their information with the new data.
* If not found, returns `404`.

### ❌ Delete User

```python
@app.delete("/deleteuser/{user_no}")
def delete_user(user_no: int):
    for index, user in enumerate(users):
        if user["no"] == user_no:
            users.pop(index)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
```

* Looks for the user by `user_no`.
* Removes the user from the list if found.
* Otherwise returns a `404`.

---

## 🧪 Example Input

**POST `/createuser/`**

```json
{
  "name": "Alice",
  "no": 1
}
```

---

## ⚠️ Notes

* The data will reset on every server restart.
* No database is used (just a Python list).
* Duplicate `no` values are not allowed.
* `no` is treated as a unique identifier.

---

