from calculator import add
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert add(1.2345, 2.3456) == pytest.approx(3.5801)

def test_add_large_numbers():
    large_val = 10**50
    assert add(large_val, large_val) == 2 * 10**50

def test_add_infinity():
    inf = float('inf')
    assert add(inf, 1) == inf
    assert add(inf, inf) == inf
    assert add(-inf, -inf) == -inf