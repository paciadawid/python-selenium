from selenium.webdriver.common.by import By

from pages.base import BasePage


class CheckoutPage(BasePage):

    cart_price_selector = (By.CLASS_NAME, "cart_total_price")

    def get_product_prices(self):
        elements = self.get_elements(self.cart_price_selector)
        price_list = []
        for price_element in elements[:-1]:
            price_list.append(int(price_element.text[4:]))
        return price_list

    def get_total_amount(self):
        elements = self.get_elements(self.cart_price_selector)
        total_amount = int(elements[-1].text[4:])
        return total_amount
