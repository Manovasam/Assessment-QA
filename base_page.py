from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def click(self, by_locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).text

    def is_visible(self, by_locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))

    def go_to(self, url):
        self.driver.get(url)