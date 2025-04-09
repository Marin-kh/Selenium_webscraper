from tests.test_base import TestBase
from pages.home_page import HomePage

class TestHome(TestBase):  # <-- Fresh browser, no login
    def test_search(self):
        home_page = HomePage(self.driver)
        home_page.search("Python")
        assert "Python" in self.driver.title

    def test_welcome_banner(self):
        home_page = HomePage(self.driver)
        assert "Welcome" in home_page.get_welcome_message()