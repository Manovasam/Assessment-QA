from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    CREATE_ACCOUNT = (By.LINK_TEXT, "Create an Account")
    SIGN_IN = (By.LINK_TEXT, "Sign In")
    ACCOUNT_MENU = (By.CLASS_NAME, "customer-welcome")
    SIGN_OUT = (By.LINK_TEXT, "Sign Out")
    MY_ACCOUNT = (By.LINK_TEXT, "My Account")

    def open_register(self):
        self.click(self.CREATE_ACCOUNT)

    def open_login(self):
        self.click(self.SIGN_IN)

    def logout(self):
        self.click(self.ACCOUNT_MENU)
        self.click(self.SIGN_OUT)

    def go_to_my_account(self):
        self.click(self.ACCOUNT_MENU)
        self.click(self.MY_ACCOUNT)