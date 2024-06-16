import pytest
from calculator import add, subtract, multiply, divide, exponentiate

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (0.1, 0.2, pytest.approx(0.3)),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (-1, -1, 0),
    (0, 0, 0),
    (0.3, 0.1, pytest.approx(0.2)),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 2, -2),
    (0, 1, 0),
    (0.1, 0.2, pytest.approx(0.02)),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (1, -1, -1),
    (0.1, 0.2, pytest.approx(0.5)),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (4, 0.5, 2),
    (9, -0.5, 1/3),
])
def test_exponentiate(a, b, expected):
    assert exponentiate(a, b) == expected