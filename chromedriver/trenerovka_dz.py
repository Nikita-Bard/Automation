from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.seleniumeasy.com/lander")

# Явное ожидание: ждать появления элемента с текстом "A/B Testing"
# element = WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="/abtest"]'))
#     )
# print(f"Элемент {element.text} найден и виден")

# browser.quit()

# Найти элемент "Excellent" и проверить его наличие
trust_score = browser.find_element(By.ID, "trust-score").is_displayed()
print(trust_score)

browser.quit()
