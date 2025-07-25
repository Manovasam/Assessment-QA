from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountPage(BasePage):
    WELCOME_MSG = (By.CLASS_NAME, "greet")
    CHANGE_PASSWORD = (By.LINK_TEXT, "Change Password")

    def go_to_change_password(self):
        self.click(self.CHANGE_PASSWORD)
