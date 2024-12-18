from selenium.webdriver.common.by import By
from url import *


def test_calc(chrome_browser):
    chrome_browser.get(URL_3)
    chrome_browser.find_element(By.ID, "user-name").send_keys('standard_user')
    chrome_browser.find_element(By.ID, "password").send_keys('secret_sauce')
    chrome_browser.find_element(By.ID, "login-button").click()
    chrome_browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-backpack').click()
    chrome_browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    chrome_browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-onesie').click()
    chrome_browser.find_element(
        By.ID, "shopping_cart_container").click()
    chrome_browser.find_element(
        By.ID, "checkout").click()
    chrome_browser.find_element(By.ID, "first-name").send_keys('Nikita')
    chrome_browser.find_element(By.ID, "last-name").send_keys('Savelev')
    chrome_browser.find_element(By.ID, "postal-code").send_keys('111333')
    chrome_browser.find_element(By.ID, "continue").click()
    total_price = chrome_browser.find_element(
        By.CLASS_NAME, 'summary_total_label')
    # выводим текстовое значение без Total: $ и меняем его на
    # ничего/пустой текст
    total = total_price.text.strip().replace("Total: ", "")

    expected_total = "$58.29"
    # Проверяем, что итоговая сумма равна ожидаемой
    assert total == expected_total
    # Выводим сообщение в случае успешного выполнения
    print("Итоговая сумма равна $58.29")
