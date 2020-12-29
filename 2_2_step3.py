from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_css_selector("#num1")
    a = a_element.text
    b_element = browser.find_element_by_css_selector("#num2")
    b = b_element.text
    y=int(a)+int(b)

    select=Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(y))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()