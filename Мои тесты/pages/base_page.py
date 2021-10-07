import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # получить элемент
    def get_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return element

    def go_to_login_page(self):
        #   login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    # проверка, что элемент "спрятался" в течение таймаута
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # проверка, что элемент не появился в течение тайм-аута
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

        # метод для решения "задачки" в alert-е

    def should_be_login_link(self):
        #   assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def open_buscet(self):
        busket_link = self.browser.find_element(*BasePageLocators.VIEW_BUSKET_BUTTON)
        busket_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

































# from selenium.common.exceptions import NoSuchElementException # (имя исключения)
# from selenium.common.exceptions import NoAlertPresentException 
# from .locators import BasePageLocators
# import math
# import time

# class BasePage():
#     def __init__(self, browser, url, timeout=5):
#         self.browser = browser
#         self.url = url
#         self.browser.implicitly_wait(timeout)
        

#     def solve_quiz_and_get_code(self):
#         alert = self.browser.switch_to.alert
#         x = alert.text.split(" ")[2]
#         answer = str(math.log(abs((12 * math.sin(float(x))))))
#         alert.send_keys(answer)
#         alert.accept()
#         try:
#             alert = self.browser.switch_to.alert
#             alert_text = alert.text
#             print(f"Your code: {alert_text}")
#             alert.accept()
#         except NoAlertPresentException:
#             print("No second alert presented")

#     def open(self): 
#         self.browser.get(self.url)

#     def go_to_login_page(self):
#         link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
#         link.click()

#     def should_be_login_link(self):
#         assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    # # (is_element_present) в него будем передавать два аргумента: как искать (css, id, xpath и тд)
    # #  и собственно что искать (строку-селектор)
    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True






# class BasePage():
#     def __init__(self, browser, url):
#         self.browser = browser
#         self.url = url

#     def open(self): 
#         self.browser.get(self.url)