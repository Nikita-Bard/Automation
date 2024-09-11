from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
try:
    chrome.get('http://uitestingplayground.com/classattr')
    # Запускаем скрипт 3 раза
    for click_blue_button in range(3):
        # Кликаем на синюю кнопку
        blue_button = chrome.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        sleep(3)
        # Кликнуть на кнопку "ОК" в модальном окне
        chrome.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    chrome.quit()
