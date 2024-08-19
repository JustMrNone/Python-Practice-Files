from calculator import square
import pytest

def test_square():
    for i in range(-5, 6):
        assert square(i) == i * i 

def test_str():
    with pytest.raises(TypeError):
        square("a")