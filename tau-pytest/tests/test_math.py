import pytest

def test_one_plus_one():
    assert 1 + 1 == 2

def test_one_plus_two():
    a, b, c = 1, 2, 3
    assert a + b == c

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

# Multiplication Test ideas:
# two positive integers
# identity: multiply by 1
# zero: multiply by 0
# positive by negative
# negative by negative 
# floats

products = [
    (2, 3, 6),
    (1, 3, 3),
    (1, 0, 0),
    (1, -5, -5),
    (-3, -3, 9),
    (2.5, 6.7, 16.75)
    ]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
        assert a * b == product