import unittest

from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.products import ProductsPage


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.home_page = HomePage()
        self.cart_page = CartPage()
        self.products_page = ProductsPage()
        self.checkout_page = CheckoutPage()

    def test_different_products_price(self):
        self.login_page.login_with_email_password("seleniumremote@gmail.com", "tester")
        self.products_page.navigate_to_product_page()
        self.products_page.add_item_to_basket("Men tshirt")
        self.products_page.add_item_to_basket("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()

        self.assertEqual(sum(self.checkout_page.get_product_prices()), self.checkout_page.get_total_amount())

    def test_10_items_of_single_product(self):
        self.login_page.login_with_email_password("seleniumremote@gmail.com", "tester")
        self.products_page.navigate_to_product_page()
        self.products_page.add_item_to_basket("unicorn", 10)
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()

        self.assertEqual(sum(self.checkout_page.get_product_prices()), self.checkout_page.get_total_amount())

    def test_checkout_for_unlogged_user(self):
        self.products_page.navigate_to_product_page()
        self.products_page.add_item_to_basket("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.assertTrue(self.cart_page.check_login_modal())

    def tearDown(self) -> None:
        self.login_page.driver.quit()

if __name__ == '__main__':
    unittest.main()
