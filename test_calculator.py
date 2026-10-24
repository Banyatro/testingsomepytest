from calculator import Calculator
import pytest


@pytest.fixture
def test_add():
    assert Calculator().add(2.0, 3.0) == 5.0
    assert Calculator().add(-1.0, 1.0) == 0.0

def test_substract():
    assert Calculator().substract(5.0, 3.0) == 2.0
    assert Calculator().substract(1.0, 5.0) == -4.0

def test_multiply():
    assert Calculator().multiply(3.0, 3.0) == 9.0
    assert Calculator().multiply(-2.0, 4.0) == -8.0

def test_divide():
    assert Calculator().divide(10.0, 5.0) == 2.0

def test_divide_by_zero(Calculator()):
    with pytest.raises(ValueError):
        Calculator().divide(5.0, 0.0)
