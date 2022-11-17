from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):

    login_tab_selector = (By.CSS_SELECTOR, "a[href='/login']")
    product_tab_selector = (By.CSS_SELECTOR, "a[href='/products']")