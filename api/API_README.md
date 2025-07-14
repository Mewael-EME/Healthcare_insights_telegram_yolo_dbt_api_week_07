# 🩺 Healthcare Analytics API (FastAPI)

An analytical API that provides medical business insights from Telegram data. This service is built with FastAPI and connects to a PostgreSQL data warehouse populated and transformed using dbt.

---

## 🚀 Setup Instructions

### 1. Install Dependencies

Make sure you’re in the root directory and install the required packages:

```bash
pip install -r requirements.txt
```

If not using `requirements.txt`, install manually:

```bash
pip install fastapi uvicorn psycopg2-binary python-dotenv
```

---

### 2. Create `.env` File

Create a `.env` file in the `api/` or root folder with your database credentials:

```env
PG_HOST=localhost
PG_PORT=5432
PG_DB=telegram_medical
PG_USER=postgres
PG_PASS=your_password
API_KEY=your_secure_api_key
```

> 🔐 **Do NOT commit this file to version control.**

---

## 🔐 API Security (API Key)

For basic protection, include your API key as a query parameter in every request:

```
?api_key=your_secure_api_key
```

If the key is missing or incorrect, you'll receive a `403 Forbidden` error.

---

## ⚡ Running the Server

Use `uvicorn` to launch the API:

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## 📊 Example API Endpoints

| Endpoint                                                                 | Description                                      |
|-------------------------------------------------------------------------|--------------------------------------------------|
| `/api/reports/top-products?limit=10&api_key=...`                        | Returns most frequently mentioned products       |
| `/api/channels/{channel_name}/activity?api_key=...`                    | Returns posting trends for the specified channel |
| `/api/search/messages?query=paracetamol&api_key=...`                   | Search messages containing a keyword             |

---

## 📄 Swagger UI (Interactive Docs)

Once the server is running, access the Swagger documentation here:

```
http://127.0.0.1:8000/docs
```

You can test the endpoints directly from this interface.

---

## ✅ Status

- FastAPI App Structure  
- Secure DB connection using `.env`  
- API Key Auth  
- dbt model integration  
- Analytical Endpoints  
