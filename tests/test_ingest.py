from app.ingest.session import normalize

def test_normalize():
    row = {"player": "  Shohei   Ohtani ", "set": "Topps Chrome", "year": "2018", "number": "HMT1", "sport": "baseball"}
    out = normalize(row)
    assert out["player"] == "Shohei Ohtani"
    assert out["year"] == 2018
    assert out["sport"] == "Baseball"
