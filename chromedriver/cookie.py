from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

# переходим на сайт
browser.get("https://www.labirint.ru/")

# add_cookie запоминает куки
browser.add_cookie(my_cookie)

# получение инфо по конкретному куки
cookie = browser.get_cookie('cookie_policy')

print(cookie)

# получение инфо по всем кукам
cookies = browser.get_cookies()

# adelete_all_cookies удаляет все куки
# browser.delete_all_cookies()

# browser.refresh()

sleep(7)
browser.quit()
