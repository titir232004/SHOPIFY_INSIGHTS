from fastapi import APIRouter, HTTPException, Query, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from ..services.fetcher import InsightsFetcher
from ..deps import validate_shop_url
from ..models.brand import BrandContext
from ..config import settings
from ..persistence.database import get_db
from ..persistence import models

router = APIRouter(prefix="/api", tags=["insights"])


class DomainRequest(BaseModel):
    domain: str


async def _fetch_and_store(domain: str, db: AsyncSession | None = None) -> BrandContext:
    _ = validate_shop_url(domain)
    try:
        fetcher = InsightsFetcher(domain)
        ctx = await fetcher.run()

        # Save to DB if session is provided
        if db:
            brand = models.Brand(
                domain=ctx.domain,
                brand_name=ctx.brand_name,
                about=ctx.about,
            )
            db.add(brand)
            await db.commit()

        return ctx

    except ValueError as e:
        if "WEBSITE_NOT_FOUND" in str(e):
            raise HTTPException(status_code=401, detail="Website not found or unreachable")
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {e}")


@router.get("/fetch_insights", response_model=BrandContext)
async def fetch_insights_get(
    website_url: str = Query(..., description="Shopify store base URL"),
    db: AsyncSession = Depends(get_db),
):
    return await _fetch_and_store(website_url, db)


@router.post("/fetch_insights", response_model=BrandContext)
async def fetch_insights_post(
    req: DomainRequest,
    db: AsyncSession = Depends(get_db),
):
    return await _fetch_and_store(req.domain, db)
