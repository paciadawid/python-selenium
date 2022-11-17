from selenium.webdriver.common.by import By

from pages.base import BasePage


class CartPage(BasePage):

    cart_tab_selector = (By.CSS_SELECTOR, "a[href='/view_cart']")
    check_out_selector = (By.CSS_SELECTOR, ".check_out")
    proceed_modal_selector = (By.ID, "checkoutModal")

    def navigate_to_cart(self):
        self.click(self.cart_tab_selector)

    def proceed_to_checkout(self):
        self.click(self.check_out_selector)

    def check_login_modal(self):
        return self.check_if_element_exists(self.proceed_modal_selector)
