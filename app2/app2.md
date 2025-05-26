### ✅ 1. **Swagger UI (Interactive API Docs)**

When you run your FastAPI app, go to:

```
http://localhost:8000/docs
```

This opens the **Swagger UI**, where you can:

* View all endpoints
* Submit requests via UI forms (no coding needed)
* Test `POST`, `PUT`, `PATCH`, and `DELETE` with body inputs

If you want the alternative ReDoc view:

```
http://localhost:8000/redoc
```

---

### ✅ 2. **cURL Commands (Command Line)**

#### ➕ Create a user (POST)

```bash
curl -X POST "http://localhost:8000/users/" \
-H "Content-Type: application/json" \
-d '{"name": "Alice", "age": 30}'
```

#### 📥 Get all users (GET)

```bash
curl http://localhost:8000/users/
```

#### 📤 Get user by ID (GET)

```bash
curl http://localhost:8000/users/<user_id>
```

#### ♻️ Replace user (PUT)

```bash
curl -X PUT "http://localhost:8000/users/<user_id>" \
-H "Content-Type: application/json" \
-d '{"name": "Alice Smith", "age": 31}'
```

#### 🔧 Partially update user (PATCH)

```bash
curl -X PATCH "http://localhost:8000/users/<user_id>" \
-H "Content-Type: application/json" \
-d '{"age": 32}'
```

#### ❌ Delete user (DELETE)

```bash
curl -X DELETE "http://localhost:8000/users/<user_id>"
```

---

### ✅ 3. **Postman Setup**

If you prefer using Postman:

1. Set method: `POST`, `GET`, etc.
2. URL: `http://localhost:8000/users/`
3. Body tab → Choose `raw` and `JSON`
4. Add JSON data, e.g.:

```json
{
  "name": "Charlie",
  "age": 22
}
```

---


