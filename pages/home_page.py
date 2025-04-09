from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    SEARCH_BAR = (By.ID, "search-bar")
    SEARCH_BUTTON = (By.ID, "search-btn")
    WELCOME_BANNER = (By.CLASS_NAME, "welcome-text")

    def search(self, query):
        self.type(self.SEARCH_BAR, query)
        self.click(self.SEARCH_BUTTON)

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_BANNER)