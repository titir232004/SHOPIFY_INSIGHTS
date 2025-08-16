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
## Installation & Setup

### 1. Clone the Repository
git clone https://github.com/yourusername/shopify-insights.git
cd shopify-insights

2. Create a Virtual Environment
It’s recommended to use a virtual environment to avoid dependency conflicts.
python -m venv venv      
source venv/bin/activate # On Linux/macOS
venv\Scripts\activate    # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file in the root directory if not already present. Example:

DATABASE_URL=sqlite:///shopify.db
API_KEY=your_api_key_here
OTHER_SETTING=value

5. Run the Application
python app/main.py

Follow the console prompts or open the API endpoints if using FastAPI routers.

6. Run Tests

To make sure everything is working correctly:
pytest tests/

License

MIT License




