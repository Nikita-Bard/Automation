from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

browser = webdriver.Chrome()


def open_labirint():
    # переходим на сайт Лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def serch(term):
    # находим все книги по слову Python
    browser.find_element(By.ID, 'search-field').send_keys(term)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


def loading_books():
    # дожидаемся (presence_of_element_located) определленого элемента
    # на странице
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'search-tab'))
        )


def add_books():
    # добовляем все книги в корзину и считаем их кол-во
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, '.btn-tocart.buy-link')

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter


def go_to_cart():
    # переходим в корзину
    browser.get('https://www.labirint.ru/cart/')


def get_cart_counter():
    # проверяем счетчик товаров, должен быть равен числу кликов
    txt = browser.find_element(By.XPATH, '//b [text()="60"]').text
    return int(txt)


def close_browser():
    browser.quit()


def test_cart_counter():
    open_labirint()
    # передаем значение 'Python' в term
    serch('Python')
    loading_books()
    # значение counter записывается в переменную added
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    assert added == cart_counter
    close_browser()
