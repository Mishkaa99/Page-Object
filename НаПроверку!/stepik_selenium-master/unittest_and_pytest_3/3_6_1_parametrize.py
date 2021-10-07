import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

links = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('current_link', links)
def test_guest_should_see_login_link(browser, current_link):
    link = current_link
    browser.get(link)
    event = EC.text_to_be_present_in_element((By.CLASS_NAME, "quiz__typename"), "Напишите текст")
    WebDriverWait(browser, 7).until(event)
    time.sleep(2)
    input_field = browser.find_element(By.CSS_SELECTOR, '.textarea')
    answer = math.log(int(time.time()))
    input_field.click()
    input_field.send_keys(str(answer))
    time.sleep(1)
    submit_button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    submit_button.click()
    event = EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"), "Correct!")
    WebDriverWait(browser, 7).until(event)
    time.sleep(1)
