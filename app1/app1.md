FastAPI code defines two endpoints—one for the root (`/`) and another for greeting a user using both **path** and **query** parameters. 

---
### 🔍 Explanation:

* `user_name` is a **path parameter** (e.g., `/greet/Alice`)
* `age` is a **query parameter** (e.g., `/greet/Alice?age=25`, optional with default `0`)
* The root route `/` returns a simple welcome message

---

### 🔧 Example Requests:

* `GET http://localhost:8000/`
  → `{"message": "Welcome"}`

* `GET http://localhost:8000/greet/Alice`
  → `{"message": "Hello Alice, you are 0 years old."}`

* `GET http://localhost:8000/greet/Bob?age=35`
  → `{"message": "Hello Bob, you are 35 years old."}`

---

