# 🧠 Healthcare Insights Telegram Project

This project extracts data from Telegram channels, stores it in a PostgreSQL database, and transforms it using dbt for analytical insights.

---

## ⚙️ 1. Project Setup

### 🔐 Environment Variables

Create a `.env` file with the following:

```env
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=+251XXXXXX

PG_HOST=localhost
PG_PORT=5432
PG_USER=postgres
PG_PASS=2328
PG_DB=telegram_medical

📦 Install Dependencies

pip install -r requirements.txt


🛠️ 2. Running the Pipeline
📥 Scrape Telegram Data

python scrapers/scrape_telegram.py

💾 Load Data into PostgreSQL

python loaders/load_raw_to_postgres.py

🔄 Run DBT Models

Move to the dbt project directory:

cd medical_dbt

# Run all models
dbt run

# Run data tests
dbt test

🏗️ 3. Project Structure

.
├── data/
│   └── raw/telegram_messages/YYYY-MM-DD/*.json
├── scrapers/
│   └── scrape_telegram.py
├── loaders/
│   └── load_raw_to_postgres.py
├── medical_dbt/
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_telegram_messages.sql
│   │   └── marts/
│   │       ├── dims/
│   │       │   ├── dim_channels.sql
│   │       │   └── dim_dates.sql
│   │       └── facts/
│   │           └── fct_messages.sql
│   ├── schema.yml
├── .env
└── requirements.txt

🧱 4. DBT Star Schema Design
🌟 Staging

stg_telegram_messages.sql

    Extracts raw JSON fields

    Converts timestamps

    Flags image presence

🧭 Dimensions

    dim_channels.sql: Telegram channel information

    dim_dates.sql: Calendar/time dimension

📊 Fact Table

    fct_messages.sql: One row per message, joins with dimensions

    Includes message metrics (e.g., length, has_image)

📑 5. Testing and Documentation

    dbt tests: not_null, unique, custom business rules

    dbt docs: run dbt docs generate && dbt docs serve

🙋 Contributors

    Mewael Mizan Tesfay