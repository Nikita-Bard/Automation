from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/ajax")

click_button = browser.find_element(By.ID, 'ajaxButton').click()

content = WebDriverWait(browser, 20)
content.until(
    EC.text_to_be_present_in_element(
        (By.ID, 'content'), 'Data loaded with AJAX get request.')
)

print(browser.find_element(By.ID, 'content').text)

browser.quit()
