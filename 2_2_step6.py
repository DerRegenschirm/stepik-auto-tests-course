from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/execute_script.html"
	browser.get(link)

	x_element = browser.find_element_by_css_selector('#input_value')
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_css_selector('#answer')
	input1.send_keys(y)

	browser.execute_script("window.scrollBy(0,500);")

	cb=browser.find_element_by_css_selector("#robotCheckbox")
	cb.click()

	rb=browser.find_element_by_css_selector('#robotsRule')
	rb.click()

	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()