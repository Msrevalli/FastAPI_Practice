from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db import async_session
from src.books.models import Book
from src.books.schemas import BookCreate, BookRead, BookUpdate

book_router = APIRouter()

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

@book_router.get("/", response_model=List[BookRead])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    result = await session.execute(Book.select())
    books = result.scalars().all()
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookRead)
async def create_book(book: BookCreate, session: AsyncSession = Depends(get_session)):
    db_book = Book.from_orm(book)
    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book

@book_router.get("/{book_id}", response_model=BookRead)
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)):
    book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@book_router.patch("/{book_id}", response_model=BookRead)
async def update_book(book_id: int, book_update: BookUpdate, session: AsyncSession = Depends(get_session)):
    book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book_data = book_update.dict(exclude_unset=True)
    for key, value in book_data.items():
        setattr(book, key, value)

    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book

@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, session: AsyncSession = Depends(get_session)):
    book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    await session.delete(book)
    await session.commit()
    return {}
