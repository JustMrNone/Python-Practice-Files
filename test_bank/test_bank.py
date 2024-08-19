from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hi hi") == 20


def test_empty():
    assert value("") == 100


def test_numbers():
    assert value("1234567890") == 100


def test_punctuation():
    assert value(",.!?;:\-()") == 100

