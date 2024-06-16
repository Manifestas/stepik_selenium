import time

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_add_product_to_basket()