from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):

    login_tab_selector = (By.CSS_SELECTOR, "a[href='/login']")
    login_field_selector = (By.XPATH, "//input[@data-qa='login-email']")
    password_field_selector = (By.NAME, "password")
    submit_login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")

    def login_with_email_password(self, email, password):
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.login_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.submit_login_button_selector).click()
