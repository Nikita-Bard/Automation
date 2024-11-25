import pytest
# Импортируем драйвер для взаимодействия с браузером
from selenium import webdriver


@pytest.fixture()
def chrome_browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    # Все что написано после yield будет выполняться после
    # прохождения всего кода
    yield browser
    browser.quit()
