from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_items_in_the_busket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_THE_BUSCET), 'there are an items in the basket'

    def should_be_text_about_empty_basket(self):
        assert self.get_element(*BasketPageLocators.BASKET_STATUS_TEXT).text.startswith('Your basket is empty.'),\
            'there is no special text!'
