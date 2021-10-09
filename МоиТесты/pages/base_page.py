from selenium.common.exceptions import NoSuchElementException # (имя исключения)
from selenium.common.exceptions import NoAlertPresentException 
from .locators import BasePageLocators
import math
import time

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        print("Значение X:" + x)
        print("Полученное число:" + answer)
        alert.accept()
        
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text            
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def open(self): 
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    # (is_element_present) в него будем передавать два аргумента: как искать (css, id, xpath и тд)
    #  и собственно что искать (строку-селектор)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True






# class BasePage():
#     def __init__(self, browser, url):
#         self.browser = browser
#         self.url = url

#     def open(self): 
#         self.browser.get(self.url)