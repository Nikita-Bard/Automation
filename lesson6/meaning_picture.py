from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

done = WebDriverWait(browser, 15)
done.until(
    EC.text_to_be_present_in_element((By.ID, 'text'), 'Done!')
)

meaning_src = browser.find_element(By.ID, 'award')
print(meaning_src.get_attribute('src'))

browser.quit()
