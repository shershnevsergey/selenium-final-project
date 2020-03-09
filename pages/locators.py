from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BASKET_PRICE_FROM_ALERT = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')
    ADDED_ITEM_NAME_FROM_ALERT = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')
