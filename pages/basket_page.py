from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_ITEM
        ), "Product is in basket, but should not be"

    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ).text
        assert "Your basket is empty" in empty_basket_message, (
            "Empty basket message is not presented"
        )
