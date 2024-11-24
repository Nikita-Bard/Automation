from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    'name': 'cookie_policy',
    'value': '1'
}


def test_cart_counter():
    browser = webdriver.Chrome()
    # переходим на сайт Лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    # находим все книги по слову Python
    browser.find_element(By.ID, 'search-field').send_keys('Python')
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # дожидаемся (presence_of_element_located) определленого элемента
    # на странице
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'search-tab'))
    )

    # добовляем все книги в корзину и считаем их кол-во
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, '.btn-tocart.buy-link')

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    # переходим в корзину
    browser.get('https://www.labirint.ru/cart/')
    # проверяем счетчик товаров, должен быть равен числу кликов
    txt = browser.find_element(By.XPATH, '//b [text()="60"]').text
    assert counter == int(txt)

    browser.quit()
