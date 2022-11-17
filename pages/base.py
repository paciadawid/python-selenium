from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException

class BasePage:

    class Webdriver:
        def __init__(self):
            #self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            self.driver.get("https://automationexercise.com/")
            self.driver.implicitly_wait(5)

    driver = None

    def __init__(self):
        if not self.driver:
            BasePage.driver = BasePage.Webdriver().driver

    def click(self, selector: tuple):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(selector)).click()

    def send_keys(self, selector: tuple, form_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
        element.clear()
        element.send_keys(form_text)

    def get_elements(self, selector):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(selector))
        return elements

    def check_if_element_exists(self, selector):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
            return True
        except TimeoutException:
            return False