import pytest
from test.Calculator.calculator import Calculator


@pytest.mark.parametrize('num1, num2, result', [
    (5, 2, 7), (-3, -4, -7),
    (-10, 3, -7), (5.1, 1.9, 7),
    (7, 0, 7)])
def test_sum_nums(just_print_a_message, num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result


def test_div_by_zero(just_print_a_message, instance: Calculator):
    with pytest.raises(ArithmeticError):
        instance.div(7, 0)
