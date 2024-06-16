from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_USERNAME_INPUT = (By.NAME, 'login-username')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'form#add_to_basket_form button.btn-add-to-basket')
    ALERT_MESSAGE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_MESSAGE_TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner strong')
