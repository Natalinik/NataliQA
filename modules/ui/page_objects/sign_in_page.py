from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by  import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def open(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # We find the field in which we will enter the incorrect username or email address
        login_elem = self.driver.find_element("id", "login_field")

        # Entering an incorrect username or email address
        login_elem.send_keys(username)

        # We find the field in which we will enter the incorrect password
        pass_elem = self.driver.find_element(By.ID, "password")

        # Entering an incorrect password
        pass_elem.send_keys(password)

        # Find the sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulate a left mouse click
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
 