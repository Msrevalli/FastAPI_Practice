from fastapi import FastAPI
from src.books.routes import book_router
from src.db import init_db
import asyncio

app = FastAPI(title="Bookstore API")

app.include_router(book_router, prefix="/books", tags=["books"])

@app.on_event("startup")
async def on_startup():
    await init_db()
