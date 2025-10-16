"""ROI & pricing helpers (sanitized)."""
from statistics import median
from typing import Iterable, List, Optional

def _clean(prices: Iterable[float]) -> List[float]:
    return [float(p) for p in prices if p is not None and float(p) >= 0.0]

def trim_outliers(prices: Iterable[float], pct: float = 0.15) -> List[float]:
    """Drop lowest/highest pct of values (two-sided)."""
    vals = sorted(_clean(prices))
    n = len(vals)
    k = int(n * pct)
    if n <= 2 or k == 0:
        return vals
    return vals[k:n - k]

def blended_price(prices: Iterable[float]) -> Optional[float]:
    """Blend median (60%) + mean (40%) after trimming outliers."""
    vals = trim_outliers(prices)
    if not vals:
        return None
    mean = sum(vals) / len(vals)
    med = median(vals)
    return round(0.6 * med + 0.4 * mean, 2)

def roi_pct(cost: float, market: Optional[float]) -> Optional[float]:
    """Return ROI% given a cost and market price."""
    if market is None or cost is None or cost <= 0:
        return None
    return round((market - cost) / cost * 100.0, 2)
