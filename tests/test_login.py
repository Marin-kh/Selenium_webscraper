import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utilities.config import BASE_URL, TEST_USER
from time import sleep

class LoginTestBase(unittest.TestCase):
    """Base class for tests that REQUIRE login."""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(BASE_URL+'/tehran')
        cls.driver.get(BASE_URL+"/login")
        login_page = LoginPage(cls.driver)
        login_page.login(TEST_USER['username'], TEST_USER['password'])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class TestLogin(LoginTestBase):
    """Tests for login functionality."""

    def test_login_success(self):
        sleep(1)
        self.driver.get(BASE_URL+"/profile/user")
        assert not "ورود به حساب کاربری | دلتا" in self.driver.title
