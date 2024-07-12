import pytest
from calculator import Calculator

calculator = Calculator()


@pytest.mark.parametrize('num1, num2, result', [
    (5, 2, 7), (-3, -4, -7),
    (-10, 3, -7), (5.1, 1.9, 7),
    (7, 0, 7)])
def test_sum_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result


@pytest.mark.parametrize('nums, result', [
    ([], 0),
    ([1, 10, 10, 3, 15, 5, 5], 7)])
def test_avg_list(nums, result):
    calculator = Calculator()
    res = calculator.avg(nums)
    assert res == result


def test_div_positive():
    calculator = Calculator()
    res = calculator.div(14, 2)
    assert res == 7


def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(7, 0)
