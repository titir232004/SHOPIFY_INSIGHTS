from fastapi import HTTPException
from pydantic import AnyUrl, HttpUrl, ValidationError
from tldextract import extract

def validate_shop_url(url: str) -> str:
    try:
        _ = HttpUrl(url=url)  # type: ignore
    except ValidationError:
        raise HTTPException(status_code=401, detail="Invalid website URL")

    t = extract(url)
    if not t.registered_domain:
        raise HTTPException(status_code=401, detail="Website not found or invalid domain")
    return url
