from calculator import calculator
import pytest


@pytest.fixture
def calc():
    return Calculator()

def test_add():
    assert calc.add(2.0, 3.0) == 5.0
    assert calc.add(-1.0, 1.0) == 0.0

def test_substract():
    assert calc.substract(5.0, 3.0) == 2.0
    assert calc.substract(1.0, 5.0) == -4.0

def test_multiply():
    assert calc.multiply(3.0, 3.0) == 9.0
    assert calc.multiply(-2.0, 4.0) == -8.0

def test_divide():
    assert calc_divide(10.0, 5.0) == 2.0

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5.0, 0.0)
