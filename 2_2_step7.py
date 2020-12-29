import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_css_selector('input[name="firstname"]')
	input1.send_keys('Tetiana')
	input2 = browser.find_element_by_css_selector('input[name="lastname"]')
	input2.send_keys('Surname')
	input3 = browser.find_element_by_css_selector('input[name="email"]')
	input3.send_keys('kokoko@gmail.com')

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_name = "test.txt"
	file_path = os.path.join(current_dir, file_name)

	element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
	element.send_keys(file_path)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()
