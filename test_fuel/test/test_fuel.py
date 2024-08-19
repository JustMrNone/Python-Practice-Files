from fuel import convert, gauge
import pytest


def test_convert_valid_fraction():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("0/4") == 0


def test_invalid_input():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("invalid")


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/3")


def test_gauge_lower_bound():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_upper_bound():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_gauge_in_between():
    assert gauge(50) == "50%"
