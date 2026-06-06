from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_name_in_message(self, expected_product_name):
        product_name_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE
        ).text
        assert expected_product_name == product_name_in_message, (
            "Product name in success message doesn't match product page name"
        )

    def should_be_basket_total_equals_product_price(self, expected_product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_IN_MESSAGE).text
        assert expected_product_price == basket_total, "Basket total doesn't match product price"
