from twttr import shorten
def test_shorten():
    assert shorten("test = aeiouAEIOU,123") == "tst = ,123"

