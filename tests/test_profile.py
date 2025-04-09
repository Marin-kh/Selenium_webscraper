from tests.test_login import LoginTestBase
from pages.profile_page import ProfilePage
import unittest

class TestProfile(LoginTestBase):
    def test_username_display(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open_dashboard()
