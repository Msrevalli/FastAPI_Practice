from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookRead(BookCreate):
    id: int

class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
