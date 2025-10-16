"""Mock listings fetcher (no network, no keys)."""
from typing import List

EXAMPLE_PRICES = {
    "kobe topps chrome 138": [110, 115, 119, 121, 124, 180],  # 180 is an outlier
    "jordan fleer 59": [88, 92, 95, 96, 97],
}

def fetch_listings(query: str) -> List[float]:
    query = " ".join(query.lower().split())
    return EXAMPLE_PRICES.get(query, [50, 55, 60, 65])
