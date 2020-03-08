from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_basket_price_equals(self, correct_price):
        price_from_alert = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_FROM_ALERT).text
        assert price_from_alert == correct_price,\
            'price from alert {} is not equals to correct price {}'.format(price_from_alert, correct_price)

    def should_added_item_name_in_notification_equal_to_item_name(self):
        item_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        title_from_alert = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME_FROM_ALERT).text
        assert title_from_alert == item_title, \
            'name from alert {} is not equals to correct name {}'.format(title_from_alert, item_title)
