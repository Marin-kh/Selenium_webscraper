from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FooterPage(BasePage):

    def about_us(self):
        self.click((By.PARTIAL_LINK_TEXT, "درباره ما"))
        body_text = self.get_text((By.XPATH, "//h2[@class='text-3xl font-bold text-gray-800 text-center mb-6']"))
        self.back_url()
        return body_text

    def faq(self):
        self.click((By.PARTIAL_LINK_TEXT, "سوالات متداول"))
        body_text = self.get_text((By.XPATH, "//div[@class='text-[#9B0000] w-full text-center text-xl  py-8 md:text-[32px] font-semibold']"))
        self.back_url()
        return body_text

    def home_delta(self):
        self.click((By.PARTIAL_LINK_TEXT, "اجاره ملک به خارجی"))
        body_text = self.get_text((By.XPATH, "//div[@class='titleMainBox']"))
        self.back_url()
        return body_text

    def contact_us(self):
        self.click((By.PARTIAL_LINK_TEXT, "تماس با ما"))
        body_text = self.get_text((By.XPATH, "//span[@class='relative']"))
        self.back_url()
        return body_text

    def employment(self):
        self.click((By.PARTIAL_LINK_TEXT, "فرصت های شغلی"))
        body_text = self.get_text((By.XPATH, "//span[@class='relative']"))
        self.back_url()
        return body_text

    def delta_blog(self):
        self.click((By.PARTIAL_LINK_TEXT, "دلتا مگ (مجله دلتا)"))
        url = self.driver.current_url
        self.back_url()
        return url

    def advertising(self):
        self.click((By.PARTIAL_LINK_TEXT, "تبلیغات در دلتا"))
        body_text = self.get_text((By.XPATH, "//span[@class='relative']"))
        self.back_url()
        return body_text