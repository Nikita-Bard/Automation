import pytest
from test.Calculator.calculator import Calculator

@pytest.fixture
def just_print_a_message():
    print("Начали выполнять тест")
    yield # вот тут сам тест
    print("Закончили выполнять тест")

@pytest.fixture
def instance():
    return Calculator()
