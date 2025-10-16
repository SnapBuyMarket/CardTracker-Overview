"""Toy grading heuristic (sanitized).
Scores 0–100 from four 0–10 sub-features and returns a band label.
"""
from typing import Dict, Tuple

WEIGHTS = {"centering": 0.4, "corners": 0.2, "edges": 0.2, "surface": 0.2}

def _clip10(x: float) -> float:
    return max(0.0, min(10.0, float(x)))

def score(features: Dict[str, float]) -> Tuple[float, str]:
    total = 0.0
    for k, w in WEIGHTS.items():
        total += _clip10(features.get(k, 7)) * w
    pct = round((total / 10.0) * 100.0, 1)
    if pct >= 90:
        band = "Gem-Mint"
    elif pct >= 80:
        band = "Mint"
    elif pct >= 70:
        band = "Near-Mint"
    else:
        band = "Raw"
    return pct, band
