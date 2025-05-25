from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def read_root():
    return "Welocme"

@app.get('/greet/{user_name}')
async def greeting(user_name):
    return {'message':f"Hello {user_name}"}



