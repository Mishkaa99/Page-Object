from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from .locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
 
    def go_to_button_page(self):
        time.sleep(3)
        button = self.browser.find_element(By.XPATH, "//*[@id='add_to_basket_form']/button")
        button.click()

    def error(self):
        name = self.browser.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1").text
        book = self.browser.find_element(By.XPATH, "//*[@id='messages']/div[1]/div/strong").text
        assert book == name, print("Не правильно выбран товар!" + " Выбрано:" + name + " В корзине:" + book)
        

    def go_to_basket_page(self):
        time.sleep(5)
        name = self.browser.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1").text
        # name = "The shellcoder's handbook"
        basket = self.browser.find_element(By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
        basket.click()
        time.sleep(5)
        last_name = self.browser.find_element(By.XPATH, "//*[@id='basket_formset']/div/div/div[2]/h3/a").text
        assert name == last_name, print("Не правильно выбран товар!" + "Выбрано:" + name + "В корзине:" + last_name)
    
         


    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     login_link.click()

    # def should_be_login_link(self):
    #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid").click()

    # def should_be_login_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

    # Внимание, здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    
        
        