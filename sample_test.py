from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://automationexercise.com/")
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, "logo")
driver.find_element(By.PARTIAL_LINK_TEXT, "Cart")
driver.find_element(By.ID, "susbscribe_email")
driver.find_element(By.CLASS_NAME, "right")
driver.find_element(By.CLASS_NAME, "brands_products")
driver.find_element(By.CLASS_NAME, "footer-bottom")

driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
driver.find_element(By.ID, "search_product").send_keys("unicorn")
driver.find_element(By.ID, "submit_search").click()
products_explicit_wait = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CLASS_NAME, "single-products")))
# products = driver.find_elements(By.CLASS_NAME, "single-products")

assert len(products_explicit_wait) >= 3, f"List result was {len(products_explicit_wait)}"
