from app.roi.pricing import trim_outliers, blended_price, roi_pct

def test_trim_and_blend():
    prices = [100, 102, 104, 106, 500]  # outlier
    assert trim_outliers(prices) == [102, 104]
    assert blended_price(prices) == 103.2

def test_roi_pct():
    assert roi_pct(80, 100) == 25.0
    assert roi_pct(0, 100) is None
