# Magento Automation

Automation script using Selenium and Python with Page Object Model.
# Magento Automation Test Suite

This project is an automation assessment for testing core user flows on [Magento](https://magento.softwaretestingboard.com).  
It uses **Selenium WebDriver**, **Python**, and follows the **Page Object Model (POM)** design pattern.

---

# Features Automated

1. Account Sign-Up  
2. User Login  
3. Logout  
4. Change Password

---
#Project Structure

magento_automation/
│
├── tests/
│ └── test_user_flow.py # Main test runner file
│
├── pages/
│ ├── base_page.py # Base page with common methods
│ ├── home_page.py # Home and navigation actions
│ ├── signup_page.py # Sign-up page actions
│ ├── login_page.py # Login page actions
│ └── account_page.py # Change password and logout
│
├── test_data/
│ └── user_data.Manova # Sample user data for test run
│
└── README.md


