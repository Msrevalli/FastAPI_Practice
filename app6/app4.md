### 📁 Project Structure

```
bookstore/
│
├                
├── requirements.txt         # Lists dependencies like FastAPI and Uvicorn
│
├── src/                     # Source code directory
│   ├── __init__.py          # Makes `src` a Python package and  Entry point of the FastAPI app
│   ├── books/               # Book module
│   │   ├── __init__.py      # Makes `books` a Python subpackage
│   │   ├── routes.py        # Contains route definitions (endpoints)
│   │   ├── schemas.py       # Pydantic models for validation
│   │   ├── book_data.py     # In-memory data storage for books
```

---

You run the app using:

```bash
fastapi dev src\
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


---

