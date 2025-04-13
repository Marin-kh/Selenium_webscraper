from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class HomePage(BasePage):

    def buy_button(self):
        self.click((By.CSS_SELECTOR, ".shadow > .grid > div:nth-of-type(1)"))
        check = self.check_filter("buy")
        self.click((By.CSS_SELECTOR, "[data-icon='close']"))
        return check

    def rent_button(self):
        self.click((By.CSS_SELECTOR, ".shadow > .grid > div:nth-of-type(2)"))
        check = self.check_filter("rent")
        self.click((By.CSS_SELECTOR,
                            "html > body:nth-of-type(1) > div:nth-of-type(4) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > button:nth-of-type(1) > span:nth-of-type(1) > span:nth-of-type(1) > svg:nth-of-type(1) > path:nth-of-type(1)"))
        return check

    def sell_button(self):
        self.click((By.PARTIAL_LINK_TEXT, "فروش ملک"))
        check = self.check_login_page()
        return check

    def ejare_button(self):
        self.click((By.PARTIAL_LINK_TEXT, "ثبت آگهی اجاره"))
        check = self.check_login_page()
        return check

    def consultant_registery_button(self):
        self.click((By.CSS_SELECTOR, "a:nth-of-type(1) > .flex-col"))
        body_text = self.get_text((By.XPATH, "//span[@class='relative']"))
        return body_text

    def agancy_registery_button(self):
        self.click((By.CSS_SELECTOR, "a:nth-of-type(2) .font-medium"))
        body_text = self.get_text((By.XPATH, "//span[@class='relative']"))
        return body_text

    def best_agancies_button(self):
        self.click((By.CSS_SELECTOR, "a:nth-of-type(3) .font-medium"))
        body_text = self.get_text((By.XPATH, "//h1[@class=' text-lg md:text-2xl font-semibold inline-flex items-center gap-2 relative']"))
        return body_text

    def vitrin(self):
        body_text = self.get_text((By.XPATH, "//div[@class='swiper-slide relative p-1 rounded-lg py-2 overflow-hidden']"))
        self.click((By.XPATH, "//div[@class='swiper-slide relative p-1 rounded-lg py-2 overflow-hidden']"))
        return body_text

    def regions_buy(self):
        parent_div = self.element((By.CSS_SELECTOR,
                                         'div.w-full.bg-white.rounded-lg.shadow.flex.flex-col.px-8.py-10.gap-10'))
        regions = self.get_child(parent_div, (By.TAG_NAME, 'li'))
        for i in range (0,len(regions)):
            parent_div = self.element((By.CSS_SELECTOR, 'div.w-full.bg-white.rounded-lg.shadow.flex.flex-col.px-8.py-10.gap-10'))
            regions = self.get_child(parent_div, (By.TAG_NAME, 'li'))
            body_text = regions[i].text
            element = self.get_child(regions[i], (By.TAG_NAME, 'a'))
            element[0].click()
            body_text2 = self.get_text((By.XPATH, "//h1[@class='text-sm font-bold']"))
            self.driver.back()
            if not body_text in body_text2:
                return False
        return True

    def regions_rent(self):
        parent_div = self.element((By.XPATH, "//div[@class='w-full bg-white rounded-lg shadow flex flex-col px-8 py-10 gap-10'][2]"))
        regions = self.get_child(parent_div, (By.TAG_NAME, 'li'))
        for i in range(0, len(regions)):
            parent_div = self.element((By.XPATH, "//div[@class='w-full bg-white rounded-lg shadow flex flex-col px-8 py-10 gap-10'][2]"))
            regions = self.get_child(parent_div, (By.TAG_NAME, 'li'))
            body_text = regions[i].text
            element = self.get_child(regions[i], (By.TAG_NAME, 'a'))
            element[0].click()
            body_text2 = self.get_text((By.XPATH, "//h1[@class='text-sm font-bold']"))
            self.driver.back()
            if not body_text in body_text2:
                return False
        return True

    def delta_blog(self):
        # element = self.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-next .transition")
        self.click((By.CSS_SELECTOR, ".swiper-slide-next .transition"))
        body_text = self.get_text((By.CSS_SELECTOR, ".swiper-slide-next .transition"))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        body_text2 = self.get_text((By.XPATH, "//h1[@class='jeg_post_title']"))
        self.driver.close()
        if body_text == body_text2:
            return True
        else:
            return False

    def check_filter(self, type):
        sleep(1)
        body_text = self.elements((By.XPATH, "//div[@class='ant-steps-item-title']"))
        if type == "buy":
            body_text = body_text[0]
        else:
            body_text = body_text[2]
        try:
            assert body_text.text == "انتخاب نوع ملک"
            return True
        except AssertionError:
            return False

    def check_login_page(self):
        self.wait_until_visible((By.XPATH, "//span[@class='text-gray-600 text-[18px] font-semibold']"))
        body_text = self.get_text((By.XPATH, "//span[@class='text-gray-600 text-[18px] font-semibold']"))
        try:
            assert body_text == "مشخصات آگهی دهنده"
            return True
        except AssertionError:
            return False


