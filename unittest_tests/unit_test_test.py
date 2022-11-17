from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class WebDriver:

    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver

driver1 = WebDriver()
driver2 = WebDriver()
driver3 = WebDriver()