from pages.home_body import *
from tests.test_login import LoginTestBase

class TestHome(LoginTestBase):

    def test_buttons(self):
        self.home = HomePage(driver=self.driver)

        # >> Buy button test
        check_buy_button = self.home.buy_button()
        if check_buy_button:
            pass
        else:
            print("Buy button is not working!")

        # >> Rent button test
        check_rent_button = self.home.rent_button()
        if check_rent_button:
            pass
        else:
            print("Rent button is not working!")

        # >> Sell button test
        check_sell_button = self.home.sell_button()
        if check_sell_button:
            pass #باید ارجاع بدی به لاگین تا لاگین رو چک کنه
        else:
            print("Sell button is not working!")
        self.driver.back()

        # >> Ejare button test
        check_ejare_button = self.home.ejare_button()
        if check_ejare_button:
            pass #باید ارجاع بدی به لاگین تا لاگین رو چک کنه
        else:
            print("Sell button is not working!")
        self.driver.back()

        # >> Consultant registery button test
        body_text_consultant = self.home.consultant_registery_button()
        try:
            assert body_text_consultant == "عضویت مشاور مستقل"
        except AssertionError:
            print("Consultant registery button is not working!")
        self.driver.back()

        # >> Agancy register button test
        body_text_agency = self.home.agancy_registery_button()
        try:
            assert body_text_agency == "عضویت آژانس املاک"
        except AssertionError:
            print("Consultant registery button is not working!")
        self.driver.back()

        # >> Best agencies button test
        body_text_best = self.home.best_agancies_button()
        try:
            assert body_text_best == "آژانس های برگزیده در تهران"
        except AssertionError:
            print("best agencies button is not working!")
        self.driver.back()

        # >> vitrin test
        body_text_vitrin = self.home.vitrin()
        words = body_text_vitrin.split()
        index_of_tehran = words.index("تهران")
        after_tehran = " ".join(words[index_of_tehran + 1:])
        body_text_vitrin2 = self.driver.find_element(By.XPATH, "//p[@class='font-DanaFanumMedium text-base text-gray-500']").text
        start_index = body_text_vitrin2.find("تهران") + len("تهران")
        end_index = body_text_vitrin2.find("،", start_index)
        result = body_text_vitrin2[start_index:end_index].strip()
        try:
            assert result == after_tehran
        except AssertionError:
            print("vitrin is not working!")
        self.driver.back()

        # >> Regions buy test
        check_region_buy = self.home.regions_buy()
        if check_region_buy:
            pass
        else:
            print("Regions button for sell is not working!")

        # >> Regions rant test
        check_region_rent = self.home.regions_rent()
        if check_region_rent:
            pass
        else:
            print("Regions button for rent is not working!")

        # >> Delta blog test
        check_delta_blog = self.home.delta_blog()
        if check_delta_blog:
            pass
        else:
            print("Delta blog button is not working!")
