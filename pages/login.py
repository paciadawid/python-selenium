from selenium.webdriver.common.by import By
import requests
from pages.base import BasePage


class LoginPage(BasePage):

    login_url = "https://automationexercise.com/login"
    login_tab_selector = (By.CSS_SELECTOR, "a[href='/login']")
    login_field_selector = (By.XPATH, "//input[@data-qa='login-email']")
    password_field_selector = (By.NAME, "password")
    submit_login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")

    def login_with_email_password(self, email, password):
        self.click(self.login_tab_selector)
        self.send_keys(self.login_field_selector, email)
        self.send_keys(self.password_field_selector, password)
        self.click(self.submit_login_button_selector)

    def login_using_api(self, email, password):
        pass
