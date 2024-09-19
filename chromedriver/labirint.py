from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

# зайти на сайт лабиринт
driver.get("https://www.labirint.ru/")

# найти книги со словом "Python"
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python", Keys.RETURN)

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

# вывести в консоль инфо: название, автор и цену книги

for book in books:
    title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
    price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text

    author = ''
    try:
        author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
    except:
        author = 'Автор не найден'

    print(author + '\t' + title + '\t' + price)

sleep(15)
