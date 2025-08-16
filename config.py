import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "shopify-insights")
    ENV = os.getenv("ENV", "dev")
    DB_URL = os.getenv("DB_URL", "")
    HTTP_TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "20"))
    HTTP_MAX_CONNECTIONS = int(os.getenv("HTTP_MAX_CONNECTIONS", "20"))
    USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0 (InsightsFetcher)")
    ENABLE_PERSISTENCE = bool(os.getenv("DB_URL"))


settings = Settings()
