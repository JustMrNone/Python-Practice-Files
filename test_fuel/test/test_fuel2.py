import pytest
from fuel import convert, gauge

def test_convert_valid_fraction():
    assert convert("3/4") == 75

def test_convert_invalid_fraction_format():
    with pytest.raises(ValueError):
        convert("invalid")

def test_convert_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/3")

def test_gauge_below_1():
    assert gauge(0) == "E"

def test_gauge_above_99():
    assert gauge(100) == "F"

def test_gauge_between_1_and_99():
    assert gauge(50) == "50%"

def test_gauge_1():
    assert gauge(1) == "E"

def test_gauge_99():
    assert gauge(99) == "F"

def test_convert_rounding():
    assert convert("1/3") == 33

def test_convert_large_fraction():
    assert convert("7/8") == 88

def test_gauge_mid_range():
    assert gauge(50) == "50%"

def test_gauge_low_boundary():
    assert gauge(2) == "2%"

def test_gauge_high_boundary():
    assert gauge(98) == "98%"

