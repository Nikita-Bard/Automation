from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("http://uitestingplayground.com/progressbar")

browser.find_element(By.ID, 'startButton').click()

# выполняем "явное" ожидание 30 секунд, запрос ходит с интервалом 0.1
# по мере выполнения опред. условия text_to_be_present_in_element
# в 75% кликнуть кнопку стоп и вывести текст на экран
waiter = WebDriverWait(browser, 30, 0.1)
waiter.until(
    EC.text_to_be_present_in_element((By.ID, 'progressBar'), '75%')
)

browser.find_element(By.ID, 'stopButton').click()

print(browser.find_element(By.ID, 'result').text)

browser.quit()
