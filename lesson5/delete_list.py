from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

try:
    chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")

    for _ in range(5):
        # Нажимаем на кнопку Add Elemet 5 раз
        click_element = chrome.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        sleep(1)
        # Собираем список кнопок Delete
        chrome_delete_buttons = chrome.find_elements(
            By.XPATH, '//button[text()="Delete"]')
    # Выводим на экран колличество кнопок Delete
    print(
        f"Колличество кнопок Delete в Chrome: {len(chrome_delete_buttons)}")

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
