import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
def test_links(browser, link):
    print(f"start test {link}")
    browser.get(link)
    input_area = browser.find_element_by_css_selector("#ember90")
    answer = math.log(int(time.time()-0.2))
    input_area.send_keys(answer)
    btn = browser.find_element_by_css_selector("button.submit-submission")
    btn.click()
    output_area = WebDriverWait(browser, 5).until(
        EC.visibility_of((By.CLASS, "smart-hints__feedback"))
    )
    output_text=output_area.text
    assert output_text == "Correct!", f"other text - {output_text}"

