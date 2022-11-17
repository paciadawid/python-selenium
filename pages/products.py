from selenium.webdriver.common.by import By

from pages.base import BasePage


class ProductsPage(BasePage):

    product_tab_selector = (By.CSS_SELECTOR, "a[href='/products']")
    search_product_selector = (By.ID, "search_product")
    submit_search_button = (By.ID, "submit_search")
    add_to_cart_selector = (By.CSS_SELECTOR, ".add-to-cart")
    continue_shopping = (By.CSS_SELECTOR, ".close-modal")
    view_cart_selector = (By.XPATH, "//a[@href='/view_cart']")

    def navigate_to_product_page(self):
        self.click(self.product_tab_selector)

    def add_item_to_basket(self, name, num_of_items=1):
        self.send_keys(self.search_product_selector, name)
        self.click(self.submit_search_button)
        for _ in range(num_of_items):
            self.click(self.add_to_cart_selector)
            self.click(self.continue_shopping)
