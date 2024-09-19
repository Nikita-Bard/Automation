from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/visibility")

# Проверяем is_displayed отображается ли элемент на странице, 
# возвращает True или False
is_displayed = browser.find_element(By.ID, 'transparentButton').is_displayed()
print(is_displayed)

click_hide = browser.find_element(By.ID, 'hideButton').click()
sleep(3)

is_displayed = browser.find_element(By.ID, 'transparentButton').is_displayed()
print(is_displayed)
sleep(3)

browser.quit()
