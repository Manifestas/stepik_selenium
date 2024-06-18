from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        # проверка на корректный url адрес
        login_url = '/basket'
        assert login_url in self.browser.current_url, "Basket url not found"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            'Product in basket presented, but should not be'

    def should_see_products_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEM), 'Product in basket not found'

    def should_see_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Empty basket message not found'

    def should_empty_basket_message_disappear(self):
        assert self.is_disappeared(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            'Emtpy basket message is not disappear, but should be'

    def should_not_see_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            'Empty basket message is presented, but should not be'

    def should_be_empty_basket(self):
        self.should_be_basket_url()
        self.should_not_be_products_in_basket()
        self.should_see_empty_basket_message()
