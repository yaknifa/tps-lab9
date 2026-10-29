import pytest

def add(a, b):
    return a + b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b

class TestMath:
    @pytest.mark.parametrize("a, b, exp", [
        (10, 5, 15),
        (-3, 3, 0),
        (0, 0, 0),
        (2.5, 2.5, 5.0)
    ])
    def test_add(self, a, b, exp):
        assert add(a, b) == exp

    @pytest.mark.parametrize("a, b, exp", [
        (20, 4, 5.0),
        (9, 3, 3.0),
        (-10, 2, -5.0)
    ])
    def test_div(self, a, b, exp):
        assert div(a, b) == exp

    def test_div_zero(self):
        with pytest.raises(ZeroDivisionError):
            div(10, 0)
