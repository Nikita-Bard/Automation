from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://demoqa.com/radio-button")

# Проверяем is_enabled доступен ли элемент для нажатия
is_enabled = browser.find_element(By.ID, 'yesRadio').is_enabled()
print(is_enabled)

is_enabled = browser.find_element(By.ID, 'noRadio').is_enabled()
print(is_enabled)

sleep(3)

browser.quit()
