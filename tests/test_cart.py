import unittest
from pages.login import LoginPage

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.login_page = LoginPage()

    def test_something(self):
        self.login_page.login_with_email_password("seleniumremote@gmail.com", "tester")

    def tearDown(self) -> None:
        self.login_page.driver.quit()

if __name__ == '__main__':
    unittest.main()
