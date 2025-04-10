import pytest
from test.Calculator.calculator import Calculator


@pytest.mark.parametrize('nums, result', [
    ([], 0),
    ([1, 10, 10, 3, 15, 5, 5], 7)])
def test_avg_list(just_print_a_message, nums, result, instance: Calculator):
    assert instance.avg(nums) == result
