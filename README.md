# CardTracker — Overview (Sanitized)
Flask app + pricing/ROI pipeline (code only, no private data/keys).

### Highlights
- **Runnable in minutes** — `python app/cardtracker_app.py` → open `http://127.0.0.1:5099/dash`.
- **ROI helpers** — `app/roi/pricing.py` (`trim_outliers`, `blended_price`, `roi_pct`).
- **Grading heuristic** — `app/grading/heuristics.py` → returns % score + band.
- **Ingest normalizer** — `app/ingest/session.py` cleans a raw card row.
- **Tests** — `tests/` with pytest; run `pytest -q`.
