from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_visability_of_element(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    element = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="add_to_basket_form"]/button')))
    assert element is not None, 'There should have been a button.'
