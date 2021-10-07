from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_item_to_the_buscet(self):
        self.should_be_buscet_button()
        self.click_to_add_to_buscet_button()

    def should_be_buscet_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BUSCET_BUTTON), "Add button is not presented"

    def click_to_add_to_buscet_button(self):
        addButton = self.get_element(*ProductPageLocators.ADD_TO_BUSCET_BUTTON)
        if addButton:
            addButton.click()

    def get_product_name_in_the_message(self):
        item_name_added_to_buscet = self.get_element(*ProductPageLocators.ITEM_NAME_MESSAGE).text
        return item_name_added_to_buscet[:item_name_added_to_buscet.find(' has been added to your basket.')]

    def get_product_name(self):
        return self.get_element(*ProductPageLocators.ITEM_NAME).text

    def check_product_name_in_the_buscet(self):
        assert self.get_product_name_in_the_message() == self.get_product_name(), \
            "There is a difference between item name and item name added to buscet"

    def get_product_price_added_to_buscet(self):
        return self.get_element(*ProductPageLocators.ITEM_PRICE_MESSAGE).text

    def get_product_price(self):
        return self.get_element(*ProductPageLocators.ITEM_PRICE).text

    def check_product_price_in_the_buscet(self):
        assert self.get_product_price_added_to_buscet() == self.get_product_price(),\
            "There is a difference between item price and price of added to buscet"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'There is a message of successfull added item when its not'

    def should_not_be_success_message_after_timeout(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is not hiding after timeout'