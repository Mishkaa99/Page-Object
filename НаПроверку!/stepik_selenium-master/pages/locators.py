from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BUSKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, 'registration_submit')
    REGISTER_SUCCESS = (By.CSS_SELECTOR, '.wicon')


class MainPageLocators:
    pass


class ProductPageLocators:
    ADD_TO_BUSCET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ITEM_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alert-info > .alertinner > p > strong')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

class BasketPageLocators:
    ITEMS_IN_THE_BUSCET = (By.CSS_SELECTOR, '#basket_formset')
    BASKET_STATUS_TEXT = (By.CSS_SELECTOR, '#content_inner p')
