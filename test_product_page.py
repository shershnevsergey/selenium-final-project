import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        current_timestamp = str(time.time())
        login_page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/accounts/login/')
        login_page.open()
        login_page.register_new_user('fakeemail{}@email.com'.format(current_timestamp), current_timestamp)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        product_page.open()
        product_page.add_to_basket()
        product_page.should_added_item_title_equals(product_page.get_product_title())
        product_page.should_basket_price_equals(product_page.get_product_price())

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        product_page.open()
        product_page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product_page.open()
    product_page.add_to_basket()
    product_page.should_added_item_title_equals(product_page.get_product_title())
    product_page.should_basket_price_equals(product_page.get_product_price())


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/', 0)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/', 0)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url, 1)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_text_message()
