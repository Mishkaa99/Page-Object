from selenium import webdriver
import pytest
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('namber', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, namber):
    link = f"https://stepik.org/lesson/{namber}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element_by_tag_name("textarea").send_keys(str(math.log(int(time.time()))))   
    time.sleep(0.3)
    browser.find_element_by_class_name("submit-submission").click()   
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("pre")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта   
    assert("Correct!" == welcome_text), print("Послание:"+ welcome_text)
    time.sleep(10)