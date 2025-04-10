from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    def loading_books(self):
        # дожидаемся (presence_of_element_located) определленого элемента
        # на странице
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-tab'))
        )

    def add_books(self):
        # добовляем все книги в корзину и считаем их кол-во
        buy_buttons = self._driver.find_elements(
            By.CSS_SELECTOR, '.btn-tocart.buy-link')

        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1

        return counter

    def get_empty_result_message(self):
        div = self._driver.find_element(By.CSS_SELECTOR, 'div.data-title')
        h1 = div.find_element(By.CSS_SELECTOR, 'h1')
        return h1.text
