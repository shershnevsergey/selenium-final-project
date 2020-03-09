from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_basket_price_equals(self, correct_price):
        price_from_alert = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_FROM_ALERT).text
        assert price_from_alert == correct_price,\
            'price from alert {} is not equals to correct price {}'.format(price_from_alert, correct_price)

    def should_added_item_title_equals(self, correct_title):
        title_from_alert = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME_FROM_ALERT).text
        assert title_from_alert == correct_title, \
            'name from alert {} is not equals to correct title {}'.format(title_from_alert, correct_title)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_ITEM_NAME_FROM_ALERT),\
            'Success message is presented, but should not be'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_ITEM_NAME_FROM_ALERT),\
            'Success message is presented and is not disappeared'
