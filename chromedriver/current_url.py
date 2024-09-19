from selenium import webdriver

browser = webdriver.Chrome()

# переходим на сайт
browser.get("https://www.ya.ru/")
# current_url возвращает "адресc" сайта
url = browser.current_url

print(url)

browser.quit()
