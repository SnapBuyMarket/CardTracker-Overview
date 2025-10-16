"""Minimal record normalizer for a card row (sanitized)."""
from typing import Dict

REQUIRED = ("player", "set", "year", "number", "sport")

def normalize(row: Dict) -> Dict:
    out = {k: (row.get(k) or "").strip() for k in REQUIRED}
    try:
        out["year"] = int(out["year"])
    except Exception:
        out["year"] = None
    out["player"] = " ".join(out["player"].split())
    out["sport"] = out["sport"].capitalize() if out["sport"] else ""
    return out
