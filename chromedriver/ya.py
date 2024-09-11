from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://ya.ru")
sleep(5)

driver.quit()
