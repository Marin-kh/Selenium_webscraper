from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    DASHBOARD_BUTTON = (By.XPATH, "//button[contains(@class, 'ant-btn')]/div[not (contains(@class, 'gap-1'))]/div")
    DASHBOARD_URL = 'https://deltadev.ir/profile/user'

    def open_dashboard(self):
        self.wait_until_visible(self.DASHBOARD_BUTTON)
        self.open_url(self.DASHBOARD_URL)