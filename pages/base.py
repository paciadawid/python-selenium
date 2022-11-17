from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BasePage:

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get("https://automationexercise.com/")
    driver.implicitly_wait(5)

    def click(self, selector: tuple):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(selector)).click()

    def send_keys(self, selector: tuple, form_text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector)).send_keys(form_text)