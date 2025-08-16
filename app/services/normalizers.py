from typing import Dict, List
from ..models.brand import Product

def normalize_products(raw_products: List[Dict], base: str) -> List[Product]:
    out = []
    for p in raw_products:
        images = [img.get("src") for img in p.get("images", []) if img.get("src")]
        variants = p.get("variants", [])
        prices = [float(v.get("price", 0) or 0) for v in variants if "price" in v]
        out.append(Product(
            id=p.get("id"),
            title=p.get("title","").strip(),
            handle=p.get("handle"),
            url=f"{base}products/{p.get('handle')}" if p.get("handle") else None,
            vendor=p.get("vendor"),
            product_type=p.get("product_type"),
            tags=p.get("tags", []),
            images=images,
            price_min=min(prices) if prices else None,
            price_max=max(prices) if prices else None,
            available=any(v.get("available") for v in variants) if variants else None
        ))
    return out
