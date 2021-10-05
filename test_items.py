from selenium import webdriver
import pytest
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button").click()   
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_xpath("//*[@id='messages']/div[1]/div/strong")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта   
    assert("Coders at Work" == welcome_text), print("Ошибка:"+ welcome_text)
    time.sleep(30)