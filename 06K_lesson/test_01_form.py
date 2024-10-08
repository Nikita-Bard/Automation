from selenium.webdriver.common.by import By
from url import *
from start_closing import *


def test_check(chrome_browser):
    chrome_browser.implicitly_wait(4)
    chrome_browser.get(URL_1)
    chrome_browser.find_element(By.NAME, "first-name").send_keys('Иван')
    chrome_browser.find_element(By.NAME, "last-name").send_keys('Петров')
    chrome_browser.find_element(By.NAME, "address").send_keys(
        'Ленина, 55-3')
    chrome_browser.find_element(By.NAME, "e-mail").send_keys('test@skypro.com')
    chrome_browser.find_element(By.NAME, "phone").send_keys('+7985899998787')
    chrome_browser.find_element(By.NAME, "city").send_keys('Москва')
    chrome_browser.find_element(By.NAME, "country").send_keys('Россия')
    chrome_browser.find_element(By.NAME, "job-position").send_keys('QA')
    chrome_browser.find_element(By.NAME, "company").send_keys('SkyPro')

    chrome_browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    assert 'danger' in chrome_browser.find_element(
        By.ID, 'zip-code').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'first-name').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'last-name').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'address').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'city').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'country').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'e-mail').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'phone').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'job-position').get_attribute('class')
    assert 'success' in chrome_browser.find_element(
        By.ID, 'company').get_attribute('class')
