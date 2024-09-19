from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://google.com")

element = browser.find_element(By.ID, "APjFqb")
element.send_keys('Тест автоматизации', Keys.RETURN)
# Очистить введеный текст
# element.clear()

sleep(7)

browser.quit()
