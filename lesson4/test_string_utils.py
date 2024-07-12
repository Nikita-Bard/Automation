import pytest
from string_utils import StringUtils

utils = StringUtils()


def test_capitalize():
    # Позитивные проверки
    assert utils.capitalize('skypro') == 'Skypro'
    assert utils.capitalize('hi friend') == 'Hi friend'
    assert utils.capitalize('321') == '321'
    # Негативные проверки
    assert utils.capitalize('') == ''
    assert utils.capitalize(' ') == ' '
    assert utils.capitalize('321тест') == '321тест'


def test_trim():
    # Позитивные проверки
    assert utils.trim('   skypro') == 'skypro'
    assert utils.trim(' hello ') == 'hello '
    assert utils.trim('  HI  ') == 'HI  '
    assert utils.trim(' ') == ''
    # Негативные проверки
    assert utils.trim('') == ''


@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(321) == '321'


@pytest.mark.parametrize('string, delimeter, result', [
    # Позитивные проверки
    ('3,2,1', ',', ['3', '2', '1']),
    ('апельсин,виноград,черешня', ',', ['апельсин', 'виноград', 'черешня']),
    ('@,%,#', ',', ['@', '%', '#']),
    # Негативные проверки
    ('', None, []),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [

    # Позитивные проверки
    ('Жвачка', 'Ж', True),
    ('Мир', 'и', True),
    ('Дружба', 'о', False),
    # Негативные проверки
    ('Ведро', 'оп', False),
    ('Рембо', '№', False),
    # ('Пончик', '', False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [

    # Позитивные проверки
    ('SkyPro', 'P', 'Skyro'),
    ('321', '2', '31'),
    ('SkyPro', 'Sky', 'Pro'),
    ('Sky Pro', ' ', 'SkyPro'),
    # Негативные проверки
    ('SkyPro', 'h', 'SkyPro'),
    ('SkyPro', '', 'SkyPro')
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки
    ('Диво', 'Д', True),
    ('Река', 'В', False),
    ('Петя', 'я', False),
    ('Течет ручей', 'р', False),
    (' ', ' ', True),
    # Негативные проверки
    (' Мороженное', ' ', True),
    ('яблоко', 'Я', False),
    ('Яблоко', 'я', False),
    (' ', '!', False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки
    ('Диво', 'о', True),
    ('Река', 'в', False),
    ('Петя', 'Я', False),
    ('Течет ручей', 'й', True),
    (' ', ' ', True),
    # Негативные проверки
    ('Мороженное ', ' ', True),
    ('яблоко', 'О', False),
    ('ЯблокО', 'о', False),
    (' ', '!', False),
    ('Вербовать', 'ть', True)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [
    # Позитивные проверки
    ('', True),
    (' ', True),
    ('   ', True),
    # Негативные проверки
    ('пусто', False),
    ('321 ', False),
    (' проверка сверка ', False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.parametrize('lst, joiner, result', [
    # Позитивные проверки
    (['3', '2', '1'], ',', '3,2,1'),
    (['a', 'b', 'c'], ',', 'a,b,c'),
    (['море', 'камень', 'солнце'], ' ', 'море камень солнце'),
    # Негативные проверки
    (['3', '2', '1'], None, '3, 2, 1'),
    ([], '', ''),
    ([], '-', '')
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
