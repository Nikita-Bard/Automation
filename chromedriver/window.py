from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.ya.ru/")

# задаём определенный размер окна
browser.set_window_size(900, 900)
sleep(7)
