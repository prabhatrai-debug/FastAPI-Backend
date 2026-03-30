# 🔐 FastAPI JWT Authentication with Role-Based Access Control

A backend authentication system built with **FastAPI**, **SQLAlchemy**, **MySQL**, and **JWT tokens**, featuring role-based access control (RBAC).

---

## 📁 Project Structure

```
├── main.py            # Core FastAPI app — routes, JWT logic, role guards
├── model.py           # SQLAlchemy User model (DB table definition)
├── schemas.py         # Pydantic schemas for request validation
├── utils.py           # Password hashing & verification (Argon2)
├── auth_database.py   # DB connection, engine, session setup
├── auth_table.py      # Creates DB tables on run
├── key.py             # Secret key generator utility
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| FastAPI | Web framework |
| SQLAlchemy | ORM for database interaction |
| MySQL (PyMySQL) | Relational database |
| python-jose | JWT encoding/decoding |
| passlib (Argon2) | Secure password hashing |
| Pydantic | Request body validation |

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql python-jose passlib[argon2] pydantic[email]
```

### 2. Configure the Database

Edit `auth_database.py` with your MySQL credentials:

```python
MYSQL_USER     = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_HOST     = "localhost"
MYSQL_PORT     = "3306"
MYSQL_DATABASE = "fastapi_db"
```

Make sure the database `fastapi_db` exists in MySQL:

```sql
CREATE DATABASE fastapi_db;
```

### 3. Create Tables

```bash
python auth_table.py
```

### 4. Generate a Secret Key (one-time)

```bash
python key.py
```

Copy the output and paste it as `SECRET_KEY` in `main.py`.

### 5. Run the Server

```bash
uvicorn main:app --reload
```

API will be live at: `http://127.0.0.1:8000`  
Swagger docs at: `http://127.0.0.1:8000/docs`

---

## 📡 API Endpoints

### 🔓 Public Routes

| Method | Endpoint | Description |
|---|---|---|
| POST | `/signup` | Register a new user |
| POST | `/login` | Login and receive a JWT token |

### 🔒 Protected Routes (Require Bearer Token)

| Method | Endpoint | Allowed Roles |
|---|---|---|
| GET | `/protected` | Any authenticated user |
| GET | `/profile` | `user`, `admin`, `civil engineer` |
| GET | `/user/dashboard` | `user`, `civil engineer` |
| GET | `/admin/dashboard` | `admin` only |

---

## 🧾 Request Examples

### Signup

```json
POST /signup
{
  "username": "john",
  "email": "john@example.com",
  "password": "secret123",
  "role": "admin"
}
```

### Login

Use form data (`OAuth2PasswordRequestForm`):

```
username=john
password=secret123
```

Returns:

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

### Accessing a Protected Route

```
GET /profile
Authorization: Bearer <jwt_token>
```

---

## 🔑 How JWT Works Here

1. On login, the server creates a JWT containing `username` and `role`, signed with `SECRET_KEY`.
2. The client sends this token in the `Authorization: Bearer <token>` header.
3. `get_current_user()` decodes and validates the token on every protected request.
4. `require_roles([...])` checks if the user's role matches the allowed roles for that route.

---

## 🛡️ Available Roles

| Role | Access |
|---|---|
| `user` | Profile, User Dashboard |
| `civil engineer` | Profile, User Dashboard |
| `admin` | Profile, Admin Dashboard |

---

## ⚠️ Security Notes

- Never commit your `SECRET_KEY` to version control — use environment variables in production.
- The Argon2 hashing algorithm is used for passwords (more secure than bcrypt).
- Token expiry is set to **30 minutes** (`ACCESS_TOKEN_EXPIRE_MINUTES`).

---

## 📌 Environment Variable Recommendation (Production)

```python
import os
SECRET_KEY = os.getenv("SECRET_KEY")
```

```bash
export SECRET_KEY="your_generated_key_here"
```