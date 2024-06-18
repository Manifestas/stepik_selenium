from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'a.btn[href *= "/basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_USERNAME_INPUT = (By.NAME, 'login-username')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '#register_form input[name="registration-email"]')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '#register_form input[name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, '#register_form input[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'form#add_to_basket_form button.btn-add-to-basket')
    ALERT_MESSAGE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_MESSAGE_TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner strong')


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, '#basket_formset .basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p>a')
