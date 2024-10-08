from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import *
from start_closing import *


def test_calc(chrome_browser):
    chrome_browser.get(URL_2)
    chrome_browser.find_element(By.ID, "delay").clear()
    chrome_browser.find_element(By.ID, "delay").send_keys('45')
    chrome_browser.find_element(
        By.XPATH, '//span[text()="7"]').click()
    chrome_browser.find_element(
        By.XPATH, '//span[text()="+"]').click()
    chrome_browser.find_element(
        By.XPATH, '//span[text()="8"]').click()
    chrome_browser.find_element(
        By.XPATH, '//span[text()="="]').click()

    WebDriverWait(chrome_browser, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))
    result_text = chrome_browser.find_element(By.CLASS_NAME, 'screen').text

    assert result_text == '15'
