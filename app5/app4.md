### 📁 Project Structure

```
bookstore/
│
├── run.py                   # Entry point of the FastAPI app
├── requirements.txt         # Lists dependencies like FastAPI and Uvicorn
│
├── src/                     # Source code directory
│   ├── __init__.py          # Makes `src` a Python package
│   ├── books/               # Book module
│   │   ├── __init__.py      # Makes `books` a Python subpackage
│   │   ├── routes.py        # Contains route definitions (endpoints)
│   │   ├── schemas.py       # Pydantic models for validation
│   │   ├── book_data.py     # In-memory data storage for books
```

---

### ✅ `run.py`

This is the **entry point** of your application. It creates a FastAPI instance and registers the router for book-related operations.

```python
from fastapi import FastAPI
from src.books.routes import book_router

app = FastAPI()

app.include_router(book_router, prefix="/api")
```

You run the app using:

```bash
uvicorn run:app --reload
```

---

### ✅ `src/books/routes.py`

This file defines all **CRUD routes** (Create, Read, Update, Delete) for books using FastAPI’s `APIRouter`.

* `GET /api/books` → Get all books
* `POST /api/books` → Add a new book
* `GET /api/book/{id}` → Get book by ID
* `PATCH /api/book/{id}` → Update a book
* `DELETE /api/book/{id}` → Delete a book

Each route interacts with `book_data.py` (a list of dictionaries) and uses validation models from `schemas.py`.

---

### ✅ `src/books/schemas.py`

This defines **Pydantic models** for request/response validation.

* `Book` — full schema used for creating and returning a book
* `BookUpdateModel` — used for partial updates (no `id` field)

These help FastAPI automatically generate documentation and validate incoming data.

---

### ✅ `src/books/book_data.py`

This acts as **mock database** using a list of dictionaries to store book records.

```python
books = [
    {
        "id": 1,
        "title": "Think Python",
        ...
    },
    ...
]
```

You can later replace this with a real database like PostgreSQL or SQLite.

---

### ✅ `requirements.txt`

Lists project dependencies:

```
fastapi
uvicorn
```

To install them:

```bash
pip install -r requirements.txt
```

---

### 🧪 How to Run the App

Use Uvicorn (ASGI server) to launch the app:

```bash
uvicorn run:app --reload
```

* `--reload` enables live reloading on code changes.
* Access Swagger UI at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

