from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_product.click()
        self.solve_quiz_and_get_code()
        self.should_be_same_price()
        self.should_be_same_name()

    def should_be_same_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert product_name == basket_name, f"different names: {product_name} vs {basket_name}"

    def should_be_same_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, f"different names: {product_price} vs {basket_price}"
