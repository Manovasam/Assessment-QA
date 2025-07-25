import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import random
from selenium import webdriver
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.change_password_page import ChangePasswordPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com")

home = HomePage(driver)
register = RegisterPage(driver)
login = LoginPage(driver)
account = AccountPage(driver)
change_pw = ChangePasswordPage(driver)

# Test Data
email = f"Manova{random.randint(1000, 9999)}@example.com"
password = "Test@12345"
new_password = "Test@54321"

# Register
home.open_register()
register.register("Test", "User", email, password)
time.sleep(5)

# Logout
home.logout()
time.sleep(5)

# Login
home.open_login()
login.login(email, password)
time.sleep(5)

# Change Password
home.go_to_my_account()
account.go_to_change_password()
change_pw.change_password(password, new_password)
time.sleep(5)

driver.quit()
