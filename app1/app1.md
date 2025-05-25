````markdown
# 🚀 FastAPI Greeting App

A minimal FastAPI application that returns a welcome message and greets users by name.

* Visit: `http://127.0.0.1:8000`

## 📘 API Endpoints

| Method | Endpoint             | Description                  |
| ------ | -------------------- | ---------------------------- |
| GET    | `/`                  | Returns a welcome message    |
| GET    | `/greet/{user_name}` | Returns a greeting with name |

### 🧪 Example

* `GET /`
  **Response:**
  `"Welocme"`

* `GET /greet/Alice`
  **Response:**

  ```json
  {
    "message": "Hello Alice"
  }
  ```

```

---

```
