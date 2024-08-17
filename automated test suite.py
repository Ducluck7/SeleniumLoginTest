import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Sets up the WebDriver
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver
        driver.get('https://semantic-ui.com/examples/login.html')

        # Finds the username (or email) and password fields and enters credentials
        username_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')

        username_field.send_keys('test@test.com')
        password_field.send_keys('test123!')
        password_field.send_keys(Keys.RETURN)

        # Checks if the login was successful
        self.assertIn('Semantic', driver.title)

    @classmethod
    def tearDownClass(cls):
        # Closes the WebDriver
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
