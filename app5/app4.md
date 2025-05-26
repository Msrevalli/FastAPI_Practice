## 📘 Overview

This app manages a list of books using **FastAPI**. It supports:

* 📖 Get all books
* ➕ Add a new book
* 🔍 Get a book by ID
* 📝 Update a book by ID
* ❌ Delete a book by ID

---

## 🗃️ Data

The app uses a hardcoded list of books stored in the variable `books`. This list acts like a fake database.

---

## 🧱 Book Models

### 📗 `Book` model

Used for reading and creating full book entries:

```python
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
```

### 📝 `BookUpdateModel`

Used for partial updates (except `id` and `published_date`):

```python
class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
```

---

## 📌 API Endpoints

### ✅ `GET /books`

Returns a list of all books.

```python
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books
```

---

### 🆕 `POST /books`

Creates a new book from the request body.

```python
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book
```

> Note: There’s no duplicate `id` check here, which could be added.

---

### 🔍 `GET /book/{book_id}`

Returns a book by its ID.

```python
@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
```

---

### ✏️ `PATCH /book/{book_id}`

Updates book fields (except ID and published\_date).

```python
@app.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language
            return book
    raise HTTPException(status_code=404, detail="Book not found")
```

---

### ❌ `DELETE /book/{book_id}`

Deletes a book by ID.

```python
@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=404, detail="Book not found")
```

---

## 🧪 Example Request

**POST** `/books`

```json
{
  "id": 7,
  "title": "Fluent Python",
  "author": "Luciano Ramalho",
  "publisher": "O'Reilly Media",
  "published_date": "2022-03-01",
  "page_count": 800,
  "language": "English"
}
```

---

## ⚠️ Limitations

* 📌 No persistent storage (data is lost when server restarts).
* 🚫 No duplicate ID check during `POST /books`.
* 🗓️ `published_date` format is a plain string; could be improved with `datetime`.

---

