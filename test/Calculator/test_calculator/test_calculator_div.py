from test.Calculator.calculator import Calculator


def test_div_positive(just_print_a_message, instance: Calculator):
    assert instance.div(14, 2) == 7
