from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Welcome"}

@app.get('/greet/{user_name}')
async def greeting(user_name: str, age: int = 0) -> dict:
    return {
        'message': f"Hello {user_name}, you are {age} years old."
    }

