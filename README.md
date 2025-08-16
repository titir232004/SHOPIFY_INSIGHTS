#Shopify Insights – GENAI Intern Project

## Overview
This project provides insights and analytics for Shopify data using Python.  
It contains modules for database creation, application logic, and testing.

## Project Structure
```
shopify-insights/
├─ app/
│  ├─ main.py
│  ├─ config.py
│  ├─ deps.py
│  ├─ utils/
│  │  ├─ url.py
│  │  ├─ text.py
│  │  └─ parsing.py
│  ├─ models/
│  │  ├─ brand.py
│  │  |─ common.py
│  │  ├─ contact.py
│  │  ├─ faq.py
│  │  ├─ policy.py
│  │  ├─ product.py
│  │  └─ social.py
│  ├─ services/
│  │  ├─ fetcher.py
│  │  ├─ extractors.py
│  │  ├─ normalizers.py
│  ├─ persistence/
│  │  ├─ database.py
│  │  ├─ models.py
│  │  └─ crud.py
│  └─ routers/
│     └─ insights.py
├─ tests/
│  ├─ test_smoke.py
│  └─ test_utils.py
├─ .env
├─ requirements.txt
```
# Shopify Insights – GENAI Intern Project

## Overview
This project provides insights and analytics for Shopify data using Python.  
It contains modules for data extraction, processing, and reporting.

## Installation

1. Clone the repository:
```
git clone https://github.com/titir232004/shopify-insights.git
cd shopify-insights
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage
Run FastAPI server:
```
uvicorn app.main:app --reload  
```
The application will start and process Shopify data, generating insights and reports based on the configurations provided.
Open a browser or Postman at http://127.0.0.1:8000/docs to see interactive API documentation.
Use the /insights endpoint to fetch brand, product, and competitor information.

## Configuration
Modify app/config.py to set database, scraping, and operational settings:
```
# Database
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "shopify_insights"

# Scraper Settings
USER_AGENT = "Mozilla/5.0"
REQUEST_TIMEOUT = 10  # seconds

# Logging
LOGGING_ENABLED = True
```
## Features
1. **Natural Language Understanding** – Processes queries and commands.  
2. **Automated Decision-Making** – Uses AI models to recommend or execute actions.  
3. **Task Automation** – Schedules and executes business tasks.  
4. **Extensible Toolset** – Add new modules for different corporate workflows.  
5. **API Integrations** – Connects with business APIs for data access.  

## Requirements
- Python 3.8+  
- Internet connection for API calls  
- Dependencies in `requirements.txt`

## License
This project is licensed under the MIT License. See LICENSE for details.



