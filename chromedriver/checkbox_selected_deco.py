from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# browser.get("https://the-internet.herokuapp.com/checkboxes")

# Проверяем is_selected в каком сейчал положении чекбокс
# cb = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')

# is_selected = cb.is_selected()
# print(is_selected)

# cb.click()

# is_selected = cb.is_selected()

# print(is_selected)

# sleep(3)

# browser.quit()

# browser.get("https://the-internet.herokuapp.com/checkboxes")

# Поиск элементов по древовидной структуре HTML
# div = browser.find_element(By.ID, 'page-footer')

# a = div.find_element(By.CSS_SELECTOR, 'a')

# print(a.get_attribute('href'))

# sleep(3)

# browser.quit()

# browser.get("https://the-internet.herokuapp.com/checkboxes")

# Ищем все элементЫ с 'div' и выводим их колличество
# divs = browser.find_elements(By.CSS_SELECTOR, 'div')
# l = len(divs)
# print(l)

# div = divs[6]

# css_class = div.get_attribute('class')
# print(css_class)

# sleep(3)

# browser.quit()

browser.get("https://demoqa.com/browser-windows")

browser.find_element(By.ID, 'tabButton').click()

# Закрывает текущую вкладку
browser.close()

sleep(10)

# Закрывает полностью браузер
browser.quit()
