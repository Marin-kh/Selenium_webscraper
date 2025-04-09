import unittest
from time import sleep
from selenium import webdriver
from utilities.config import BASE_URL


class TestBase(unittest.TestCase):
    """Base class for tests that DON'T need login."""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(BASE_URL+'/tehran')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
