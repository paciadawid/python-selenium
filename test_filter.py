import random
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestFilters(unittest.TestCase):
    login_button_selector = (By.CSS_SELECTOR, "a[href='/login']")
    login_field_selector = (By.XPATH, "//input[@data-qa='login-email']")
    password_field_selector = (By.NAME, "password")
    submit_login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")

    brands_selector = (By.XPATH, "//div[@class ='brands-name']//a")

    categories_selector = (By.CSS_SELECTOR, ".category-products>.panel")
    single_category_selector = (By.XPATH, "//*[@data-parent='#accordian']")
    subcategory_selector = (By.XPATH, "//li/a")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://automationexercise.com/")
        self.driver.implicitly_wait(5)

        self.driver.find_element(*self.login_button_selector).click()
        self.driver.find_element(*self.login_field_selector).send_keys("seleniumremote@gmail.com")
        self.driver.find_element(*self.password_field_selector).send_keys("tester")
        self.driver.find_element(*self.submit_login_button_selector).click()

    def test_category(self):
        categories = self.driver.find_elements(*self.categories_selector)
        random_category = random.choice(categories)
        random_category.find_element(*self.single_category_selector).click()
        subcategories = random_category.find_elements(*self.subcategory_selector)
        random.choice(subcategories).click()

    def test_brands(self):
        brands = self.driver.find_elements(*self.brands_selector)
        random.choice(brands).click()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
