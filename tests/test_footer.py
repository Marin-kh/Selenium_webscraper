from tests.test_base import TestBase
from pages.footer import *

class FooterTest(TestBase):

    def test_footer(self):
        self.footer = FooterPage(driver=self.driver)

        # >> About Us:
        about_us_check = self.footer.about_us()
        try:
            assert about_us_check == "درباره ما"
        except AssertionError:
            print("About us is not working")

        # >> FAQ:
        faq_check = self.footer.faq()
        try:
            assert faq_check == "شاید برای شما هم سوال باشد ..."
        except AssertionError:
            print("FAQ is not working")

        # >> home.delta
        home_delta_check = self.footer.home_delta()
        try:
            assert home_delta_check.replace("\n", " ") == "Rent Desirable Properties in Tehran"
        except AssertionError:
            print("Home.delta is not working")

        # >> Contac Us:
        contact_us_check = self.footer.contact_us()
        try:
            assert contact_us_check == "تماس با ما"
        except AssertionError:
            print("Contac us is not working")

        # >> Employment:
        employment_check = self.footer.employment()
        try:
            assert employment_check == "فرصت‌های شغلی در هلدینگ دلتا"
        except AssertionError:
            print("Employment is not working")

        # >> Delta Blog:
        delta_blog_check = self.footer.delta_blog()
        try:
            assert delta_blog_check == "https://delta.ir/blogg/"
        except AssertionError:
            print("Delta blog is not working")

        # >> Advertising:
        advertising_check = self.footer.advertising()
        try:
            assert advertising_check == "تبلیغات در دلتا"
        except AssertionError:
            print("Advertising is not working")