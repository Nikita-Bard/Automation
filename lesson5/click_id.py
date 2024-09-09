from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    count = 0
    chrome.get("http://uitestingplayground.com/dynamicid")
    firefox.get("http://uitestingplayground.com/dynamicid")
    # Кликаем на синюю кнопку
    blue_button = chrome.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    click_element = firefox.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    # Кликаем на синюю кнопку 3 раза
    for _ in range(3):
        blue_button = chrome.find_element(
            By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        click_element = firefox.find_element(
            By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)
except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()
