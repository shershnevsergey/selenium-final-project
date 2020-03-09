from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.XPATH, "//*/span/a[text()='View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BASKET_PRICE_FROM_ALERT = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')
    ADDED_ITEM_NAME_FROM_ALERT = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')


class BasketPageLocators:
    BASKET_ITEMS_CONTAINER = (By.CSS_SELECTOR, '#basket_formset .basket-items')
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p[contains(text(),'Your basket is empty')]")
