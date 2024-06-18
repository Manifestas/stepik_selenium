from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_add_product_to_basket(self):
        self.should_message_with_added_product()
        self.should_message_with_basket_sum()

    def should_message_with_added_product(self):
        product_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE_PRODUCT_ADDED_TO_BASKET).text
        assert product_text == alert_text, 'Alert message products name wrong'

    def should_message_with_basket_sum(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE_TOTAL_BASKET_PRICE).text
        assert product_price == alert_text, 'Alert message basket sum wrong'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_MESSAGE_PRODUCT_ADDED_TO_BASKET), \
            'Success message is presented, but should not be'

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_MESSAGE_PRODUCT_ADDED_TO_BASKET), \
            'Success message is not disappear, but should be'

