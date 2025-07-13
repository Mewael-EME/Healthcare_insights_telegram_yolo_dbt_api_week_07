# Healthcare Insights Telegram YOLO DBT API Project

## Project Overview

This project collects and analyzes Telegram channel data related to healthcare insights. It includes:

- Data scraping from Telegram channels
- Data storage in a structured JSON format
- Data transformation and validation using dbt with PostgreSQL
- Dockerized environment for easy setup and deployment

---

## Project Structure
/data/raw/YYYY-MM-DD/channelname.json # Raw scraped Telegram messages
/telegram_data_pipeline/ # Python scraper scripts
/medical_dbt/ # dbt project with models and tests
/Dockerfile, docker-compose.yml # Docker configuration files
requirements.txt # Python dependencies
.env # Environment variables (excluded from git)
README.md # Project documentation


---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mewael-EME/Healthcare_insights_telegram_yolo_dbt_api_week_07.git
cd Healthcare_insights_telegram_yolo_dbt_api_week_07

2. Set up Environment Variables

Create a .env file in the root directory with the following variables:
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

3. Install Python Dependencies
pip install -r requirements.txt

4. Running the Telegram Scraper

Run the data collection script to scrape messages:

python telegram_data_pipeline/scraper.py

Scraped data will be saved under:
data/raw/YYYY-MM-DD/channelname.json

5. Set up PostgreSQL and dbt

    Ensure PostgreSQL is running and accessible with credentials matching .env.

    Configure ~/.dbt/profiles.yml with:

your_project_name:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      user: your_postgres_user
      password: your_postgres_password
      port: 5432
      dbname: your_postgres_database
      schema: public
6. Run dbt Models and Tests

From medical_dbt directory:


dbt deps
dbt run
dbt test

Logging and Error Handling

The scraper logs key events including scraping start, end, message counts, and errors. Logs can be found in telegram_data_pipeline/logs/scraper.log.


Docker Setup 

To run everything via Docker:
docker-compose up --build
