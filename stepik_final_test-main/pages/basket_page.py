from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items are presented, but should not be"

    def should_be_basket_empty_text(self):
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        basket_empty_text = basket_empty.text
        assert 'empty' in basket_empty_text
