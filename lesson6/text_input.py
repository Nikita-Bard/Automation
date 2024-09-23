from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(4)

browser.get("http://uitestingplayground.com/textinput")

browser.find_element(By.ID, 'newButtonName').send_keys('SkyPro')
browser.find_element(By.ID, 'updatingButton').click()

text = browser.find_element(By.ID, "updatingButton").text
print(text)

browser.quit()
