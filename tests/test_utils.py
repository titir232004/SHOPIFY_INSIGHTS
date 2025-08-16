from app.utils.url import normalize_base

def test_normalize_base():
    assert normalize_base("memy.co.in") == "https://memy.co.in/"
    assert normalize_base("https://memy.co.in") == "https://memy.co.in/"
