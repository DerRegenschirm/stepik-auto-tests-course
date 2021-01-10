def calc():
    return str(math.log(int(time.time()-0.2)))

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
def test_links(browser, link):
    print(f"start test {link}")
    browser.get(link)

    browser.implicitly_wait(5)
#we need to wait for 5s for each element

    input_area = browser.find_element_by_css_selector(".ember-text-area")
#find the imput box

    answer = calc()
    input_area.send_keys(answer)
#calculater an answer

    btn = browser.find_element_by_css_selector("button.submit-submission")
    btn.click()
#send the answer

    output_area = browser.find_element_by_css_selector(".smart-hints__feedback")
    output_text = output_area.text
#find a new feedback box

    assert output_text == "Correct!", f"other text - {output_text}"
#compare the text

