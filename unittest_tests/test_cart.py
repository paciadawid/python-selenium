import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class TestFilters(unittest.TestCase):
    login_button_selector = (By.CSS_SELECTOR, "a[href='/login']")
    login_field_selector = (By.XPATH, "//input[@data-qa='login-email']")
    password_field_selector = (By.NAME, "password")
    submit_login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")

    product_tab_selector = (By.CSS_SELECTOR, "a[href='/products']")
    search_product_selector = (By.ID, "search_product")
    submit_search_button = (By.ID, "submit_search")
    add_to_cart_selector = (By.CSS_SELECTOR, ".add-to-cart")
    continue_shopping = (By.CSS_SELECTOR, ".close-modal")
    view_cart_selector = (By.XPATH, "//a[@href='/view_cart']")
    check_out_selector = (By.CSS_SELECTOR, ".check_out")
    cart_price_selector = (By.CLASS_NAME, "cart_total_price")

    def setUp(self) -> None:
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        self.driver.get("https://automationexercise.com/")
        self.driver.implicitly_wait(5)

        self.driver.find_element(*self.login_button_selector).click()
        self.driver.find_element(*self.login_field_selector).send_keys("seleniumremote@gmail.com")
        self.driver.find_element(*self.password_field_selector).send_keys("tester")
        self.driver.find_element(*self.submit_login_button_selector).click()

    def test_products_price_calculation(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.product_tab_selector)).click()
        self.driver.find_element(*self.search_product_selector).send_keys("Men tshirt")
        self.driver.find_element(*self.submit_search_button).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_selector)).click()
        self.driver.find_element(*self.continue_shopping).click()
        search_field = self.driver.find_element(*self.search_product_selector)
        search_field.clear()
        search_field.send_keys("unicorn")
        self.driver.find_element(*self.submit_search_button).click()
        self.driver.find_element(*self.add_to_cart_selector).click()
        self.driver.find_element(*self.view_cart_selector).click()
        self.driver.find_element(*self.check_out_selector).click()

        price_elements = self.driver.find_elements(*self.cart_price_selector)

        total_price = 0
        total_amount = int(price_elements[-1].text[4:])
        for price_element in price_elements[:-1]:
            total_price += int(price_element.text[4:])

        assert total_amount == total_price

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
