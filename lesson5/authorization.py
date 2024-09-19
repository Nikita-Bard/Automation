from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

try:
    firefox.get('http://the-internet.herokuapp.com/login')

    input_name = firefox.find_element(By.CSS_SELECTOR, "[id=username]")
    input_name.send_keys("tomsmith")
    sleep(2)
    input_pass = firefox.find_element(By.CSS_SELECTOR, "[id=password]")
    input_pass.send_keys("SuperSecretPassword!")
    sleep(2)
    click_element = firefox.find_element(
            By.CSS_SELECTOR, "[class=radius]").click()
    sleep(3)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
