**Endpoint behavior and how to call them with headers** 

## ✅ 1. **Create User**

**Endpoint:** `POST /users/`
**Headers:** `X-API-Key` (optional)
**Body (JSON):**

```json
{
  "name": "Alice",
  "age": 30
}
```

**Example cURL:**

```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: my-secret-key" \
  -d '{"name": "Alice", "age": 30}'
```

---

## ✅ 2. **Get All Users**

**Endpoint:** `GET /users/`
**Headers:** `X-Request-Id` (optional)

**Example cURL:**

```bash
curl -X GET "http://127.0.0.1:8000/users/" \
  -H "X-Request-Id: req-123"
```

**Example response:**

```json
{
  "request_id": "req-123",
  "users": [
    {
      "name": "Alice",
      "age": 30,
      "id": "f97f7b32-cf1c-4633-bef7-b2a087e0de92"
    }
  ]
}
```

---

## ✅ 3. **Patch (Update) User**

**Endpoint:** `PATCH /users/{user_id}`
**Headers:** `X-User-Role: admin` *(required to allow update)*
**Body (JSON):**

```json
{
  "age": 35
}
```

**Example cURL:**

```bash
curl -X PATCH "http://127.0.0.1:8000/users/f97f7b32-cf1c-4633-bef7-b2a087e0de92" \
  -H "Content-Type: application/json" \
  -H "X-User-Role: admin" \
  -d '{"age": 35}'
```

---

## 🔒 Security Logic

* `X-User-Role` must be `"admin"` for the `PATCH` endpoint to succeed.
* Missing or incorrect headers will return `403 Forbidden` or use default `"user"` role and block update.

---

