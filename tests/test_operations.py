import pytest
from app.operations import Operations


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-2, 2, 0),
        (2.5, 2.5, 5.0),
    ],
)
def test_add(a, b, expected):
    assert Operations.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 5, 5),
        (5, 10, -5),
        (-2, -2, 0),
        (2.5, 1.5, 1.0),
    ],
)
def test_subtract(a, b, expected):
    assert Operations.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (10, 0, 0),
        (-2, 3, -6),
        (2.5, 4, 10.0),
    ],
)
def test_multiply(a, b, expected):
    assert Operations.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (20, 4, 5),
        (-10, 2, -5),
        (1, 4, 0.25),
    ],
)
def test_divide(a, b, expected):
    assert Operations.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(10, 0)