from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routers.insights import router as insights_router
from .config import settings
from app.persistence.database import engine, Base

from app.persistence import models

app = FastAPI(title=settings.APP_NAME)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(insights_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # Auto-create tables from all registered models
        await conn.run_sync(Base.metadata.create_all)
