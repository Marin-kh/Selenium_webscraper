from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text + Keys.ENTER)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        ).text

    def open_url(self, url):
        return self.driver.get(url)

    def wait_until_visible(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator))

    def back_url(self):
        return self.driver.back()

    def element(self, locator):
        by, value = locator
        self.wait_until_visible(locator)
        return self.driver.find_element(by, value)

    def elements(self, locator):
        by, value = locator
        return self.driver.find_elements(by, value)

    def get_child(self, parent, locator):
        by, value = locator
        return parent.find_elements(by, value)