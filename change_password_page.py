from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ChangePasswordPage(BasePage):
    CURRENT = (By.ID, "current-password")
    NEW = (By.ID, "password")
    CONFIRM = (By.ID, "password-confirmation") 
    SAVE = (By.CSS_SELECTOR, "button[title='Save']")

    def change_password(self, old_pass, new_pass):
        self.enter_text(self.CURRENT, old_pass)
        self.enter_text(self.NEW, new_pass)
        self.enter_text(self.CONFIRM, new_pass)
        self.click(self.SAVE)
