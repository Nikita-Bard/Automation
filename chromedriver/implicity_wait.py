from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(20)

browser.get("http://uitestingplayground.com/ajax")

click_button = browser.find_element(By.ID, 'ajaxButton').click()

content = browser.find_element(By.ID, 'content')
txt = content.find_element(By.CLASS_NAME, "bg-success").text

print(txt)

browser.quit()
