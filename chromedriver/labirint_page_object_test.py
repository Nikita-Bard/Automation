from selenium import webdriver

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_cart_counter(driver):
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    main_page.searsh('Python')

    result_page = ResultPage(driver)
    result_page.loading_books()
    to_be = result_page.add_books()

    cart_page = CartPage(driver)
    cart_page.get()
    as_is = cart_page.get_counter()

    assert as_is == to_be


def test_empty_search_result():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.searsh('теремок, бегунок, узелок, Python')

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()

    assert msg == 'Все, что мы нашли в Лабиринте по запросу «теремок, бегунок, узелок, Python»'
    browser.quit()
