from selenium import webdriver

browser = webdriver.Chrome()

# переходим на сайт
browser.get("https://www.ya.ru/")
# title возвращает название заголовка вкладки
current_title = browser.title

print(current_title)

browser.quit()
