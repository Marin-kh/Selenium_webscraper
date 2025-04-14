from time import sleep
from pages.navar import *
from tests.test_login import LoginTestBase

class TestNavar(LoginTestBase):

    def test_navar(self):
        self.navar = Navar(driver=self.driver)

        # >> Main Page:
        main_page_check = self.navar.main_page()
        try:
            assert main_page_check == "خرید ، فروش ، رهن و اجاره خانه ، آپارتمان ، ویلا و مغازه درتهران"
        except AssertionError:
            print("Main page button is not working!")

        # >> Search for buy:
        search_for_buy_check = self.navar.serch_for_buy()
        if not search_for_buy_check:
            print("Search for buy button is not working!")

        # >> Search for rent:
        search_for_rent_check = self.navar.serch_for_rent()
        if not search_for_rent_check:
            print("Search for rent button is not working!")

        # >> Search with code:
        search_with_code_check = self.navar.search_with_code()
        if not search_with_code_check:
            print("Search with code button is not working!")

        # >> Search in map:
        search_in_map_check = self.navar.search_in_map()
        if not search_in_map_check:
            print("Search in map button is not working!")

        # >> Add property:
        add_property_check = self.navar.add_property()
        try:
            assert add_property_check == "مشخصات آگهی دهنده"
        except AssertionError:
            print("Add property button is not working!")

        # >> Add request:
        add_request_check = self.navar.add_request()
        try:
            assert add_request_check == "نوع تقاضا"
        except AssertionError:
            print("Add request button is not working!")

        # >> Employment:
        employment_check = self.navar.employment()
        try:
            employment_check == "فرصت‌های شغلی در هلدینگ دلتا"
        except AssertionError:
            print("Employment button is not working!")