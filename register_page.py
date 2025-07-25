from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    FIRSTNAME = (By.ID, "firstname")
    LASTNAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SUBMIT = (By.CSS_SELECTOR, "button[title='Create an Account']")

    def register(self, firstname, lastname, email, password):
        self.enter_text(self.FIRSTNAME, firstname)
        self.enter_text(self.LASTNAME, lastname)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.CONFIRM_PASSWORD, password)
        self.click(self.SUBMIT) 
