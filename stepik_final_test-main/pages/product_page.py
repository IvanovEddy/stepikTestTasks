from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST) is not None

    def should_be_book_name_notification(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_NOTIFICATION) is not None

    def names_are_equal(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_text = book_name.text
        book_name_notification = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_NOTIFICATION)
        book_name_notification_text = book_name_notification.text
        assert book_name_text == book_name_notification_text

    def costs_are_equal(self):
        book_cost = self.browser.find_element(*ProductPageLocators.BOOK_COST)
        book_cost_text = book_cost.text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
        basket_cost_text = basket_cost.text
        assert book_cost_text == basket_cost_text


