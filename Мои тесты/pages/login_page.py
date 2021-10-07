from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/ru/accounts/login/',\
            'Current link is not login page'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.get_element(*LoginPageLocators.REGISTRATION_LOGIN).send_keys(email)
        self.get_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_success_message(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUCCESS).text == 'Спасибо за регистрацию!',\
            'unsuccessful registration request'