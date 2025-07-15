# 🧠 Healthcare Insights Telegram Project

An end-to-end data platform that scrapes medical-related messages from public Telegram channels, transforms the data into a clean star schema using DBT, enriches it with object detection via YOLOv8, exposes analytics via FastAPI, and orchestrates it all using Dagster.

---

## 📦 1. Setup Instructions

### 🔐 Environment Variables

Create a `.env` file in the project root:

```env
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=+251XXXXXXX

PG_HOST=localhost
PG_PORT=5432
PG_USER=postgres
PG_PASS=2328
PG_DB=telegram_medical

API_KEY=your_secure_api_key
```

> ⚠️ Never commit your `.env` file to version control.

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

If not using `requirements.txt`:

```bash
pip install fastapi uvicorn dbt psycopg2-binary python-dotenv ultralytics dagster dagster-webserver
```

---

## 🛠️ 2. Running the Pipeline

### 📥 Step 1: Scrape Telegram Data

```bash
python scrapers/scrape_telegram.py
```

### 💾 Step 2: Load JSON into PostgreSQL

```bash
python loaders/load_raw_to_postgres.py
```

### 🧠 Step 3: Run YOLOv8 Object Detection (Optional for Task 3)

```bash
python enrichment/run_yolo_inference.py
```

### 🔄 Step 4: Run DBT Models

```bash
cd medical_dbt

dbt run        # Build all models
dbt test       # Run tests
dbt docs generate && dbt docs serve  # Open DBT docs
```

---

## 📊 3. Analytical API with FastAPI

### 🔥 Run the API server

```bash
cd api
uvicorn main:app --reload
```

### 🔐 API Key Security

Pass `?api_key=your_secure_api_key` in every request.

### 🧪 Example Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/reports/top-products?limit=10&api_key=...` | Most frequently mentioned products |
| `/api/channels/{channel_name}/activity?api_key=...` | Posting trends per channel |
| `/api/search/messages?query=paracetamol&api_key=...` | Search messages by keyword |

### 📄 Swagger UI

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🛠️ 4. Dagster Orchestration

Use [Dagster](https://dagster.io) to run and monitor the full pipeline.

### ⚙️ Run Dagster UI

```bash
dagster dev -w workspace.yaml
```

Open Dagit at: [http://localhost:3000](http://localhost:3000)

### 🧩 Included Dagster Ops & Job

- `scrape_telegram_data()`
- `load_raw_to_postgres()`
- `run_dbt_models()`
- `run_yolo_enrichment()`

Located in `orchestrator/ops.py` and connected via `orchestrator/jobs.py`

---

## 🧱 5. DBT Star Schema Design

### 📥 Staging

- `stg_telegram_messages.sql`: Cleans and extracts message content

### 📚 Dimensions

- `dim_channels.sql`: Metadata per Telegram channel
- `dim_dates.sql`: Time dimension for trend analysis

### 🧾 Facts

- `fct_messages.sql`: Core message facts
- `fct_image_detections.sql`: Detected object classes from YOLO

### ✅ Tests

- Primary keys: `unique`, `not_null`
- Business logic: Message must not be empty
- Custom tests included under `tests/`

---

## 🧠 6. Project Structure

```
telegram_medical_pipeline/
├── api/                    # FastAPI analytical interface
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── data/
│   └── raw/
├── loaders/
│   ├── load_raw_to_postgres.py
│   └── create_image_detections_table.py
├── enrichment/
│   └── run_yolo_inference.py
├── scrapers/
│   └── scrape_telegram.py
├── orchestrator/
│   ├── __init__.py
│   ├── jobs.py
│   ├── ops.py
│   └── schedules.py
├── medical_dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── marts/
│   │   │   ├── dims/
│   │   │   └── facts/
│   └── dbt_project.yml
├── workspace.yaml
├── pyproject.toml
├── requirements.txt
├── .env
└── README.md
```

---

## ✅ Status

- [x] ✅ Task 0: Project Setup
- [x] ✅ Task 1: Telegram Scraping
- [x] ✅ Task 2: DBT Transformation & Testing
- [x] ✅ Task 3: YOLOv8 Enrichment
- [x] ✅ Task 4: Analytical API (FastAPI)
- [x] ✅ Task 5: Dagster Orchestration

---

## 🙋 Contributor

**👨‍💻 Mewael Mizan Tesfay**  
GitHub: [@Mewael-EME](https://github.com/Mewael-EME)
