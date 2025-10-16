from app.grading.heuristics import score

def test_grading_bands():
    pct, band = score({"centering": 9, "corners": 8, "edges": 8, "surface": 9})
    assert band in {"Gem-Mint", "Mint"}
