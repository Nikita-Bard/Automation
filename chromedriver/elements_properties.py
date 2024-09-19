from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://google.com")

# Выводим название (текст) элементов в консоль
climate_txt = browser.find_element(By.CLASS_NAME, 'ktLKi').text
print(climate_txt)

# Выводим название тега в консоль
tag = browser.find_element(By.CLASS_NAME, 'ktLKi').tag_name
print(tag)

# Выводим id элемента на странице
id = browser.find_element(By.CLASS_NAME, 'ktLKi').id
print(id)

# Получаем значение атрибута href
href = browser.find_element(By.CLASS_NAME, 'pHiOh').get_attribute('href')
print(href)

# Возвращаем значение css 'font-family'
css = browser.find_element(By.CLASS_NAME, 'ktLKi').value_of_css_property('font-family')
print(css)

# Возвращаем значение css 'collor'
css_color = browser.find_element(By.CLASS_NAME, 'ktLKi').value_of_css_property('color')
print(css_color)

sleep(7)

browser.quit()
