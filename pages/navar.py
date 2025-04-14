from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_body import HomePage

class Navar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.filter = HomePage(driver=self.driver)
        self.click((By.XPATH, "/html[@class='font-ShabnamRegular']/body/div[@class='  px-3 lg:px-0']/div[@class='hidden lg:block w-full h-fit bg-white py-1 relative z-[999] shadow-[0_4px_6px_-1px_rgba(0,0,0,0.1)]']/div[@class='mx-auto max-w-7xl  px-3 lg:px-0']/div[@class='flex gap-6 py-2 text-gray-600 text-sm font-DanaFanumMedium']/div[@class='ant-dropdown-trigger ant-dropdown-rtl hover:text-red-600']/div[@class='ant-space css-1f3ldtq ant-space-horizontal ant-space-rtl ant-space-align-center ant-space-gap-row-small ant-space-gap-col-small cursor-pointer']/div[@class='ant-space-item'][1]"))
        self.searches = self.elements((By.CSS_SELECTOR, "ul.ant-dropdown-menu-root > li.ant-dropdown-menu-item"))

    def main_page(self):
        self.click((By.CSS_SELECTOR, "div.w-full.bg-white.flex.items-center.justify-between.py-2"))
        body_text = self.get_text((By.XPATH, "//h1[@class='text-gray-500 font-medium hidden md:block text-xl w-full text-center']"))
        return body_text

    def serch_for_buy(self):
        self.click((By.XPATH, "/html[@class='font-ShabnamRegular']/body/div[@class='  px-3 lg:px-0']/div[@class='hidden lg:block w-full h-fit bg-white py-1 relative z-[999] shadow-[0_4px_6px_-1px_rgba(0,0,0,0.1)]']/div[@class='mx-auto max-w-7xl  px-3 lg:px-0']/div[@class='flex gap-6 py-2 text-gray-600 text-sm font-DanaFanumMedium']/div[@class='ant-dropdown-trigger ant-dropdown-rtl hover:text-red-600']/div[@class='ant-space css-1f3ldtq ant-space-horizontal ant-space-rtl ant-space-align-center ant-space-gap-row-small ant-space-gap-col-small cursor-pointer']/div[@class='ant-space-item'][1]"))
        self.click((self.searches[0]))
        check = self.filter.check_filter("buy")
        self.click((By.CSS_SELECTOR, "[data-icon='close']"))
        return check

    def serch_for_rent(self):
        self.click((By.XPATH, "/html[@class='font-ShabnamRegular']/body/div[@class='  px-3 lg:px-0']/div[@class='hidden lg:block w-full h-fit bg-white py-1 relative z-[999] shadow-[0_4px_6px_-1px_rgba(0,0,0,0.1)]']/div[@class='mx-auto max-w-7xl  px-3 lg:px-0']/div[@class='flex gap-6 py-2 text-gray-600 text-sm font-DanaFanumMedium']/div[@class='ant-dropdown-trigger ant-dropdown-rtl hover:text-red-600']/div[@class='ant-space css-1f3ldtq ant-space-horizontal ant-space-rtl ant-space-align-center ant-space-gap-row-small ant-space-gap-col-small cursor-pointer']/div[@class='ant-space-item'][1]"))
        self.click((self.searches[1]))
        check = self.filter.check_filter("rent")
        self.click((By.CSS_SELECTOR, "html > body:nth-of-type(1) > div:nth-of-type(5) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > button:nth-of-type(1) > span:nth-of-type(1) > span:nth-of-type(1) > svg:nth-of-type(1) > path:nth-of-type(1)"))
        return check

    def search_with_code(self):
        self.click((By.XPATH, "/html[@class='font-ShabnamRegular']/body/div[@class='  px-3 lg:px-0']/div[@class='hidden lg:block w-full h-fit bg-white py-1 relative z-[999] shadow-[0_4px_6px_-1px_rgba(0,0,0,0.1)]']/div[@class='mx-auto max-w-7xl  px-3 lg:px-0']/div[@class='flex gap-6 py-2 text-gray-600 text-sm font-DanaFanumMedium']/div[@class='ant-dropdown-trigger ant-dropdown-rtl hover:text-red-600']/div[@class='ant-space css-1f3ldtq ant-space-horizontal ant-space-rtl ant-space-align-center ant-space-gap-row-small ant-space-gap-col-small cursor-pointer']/div[@class='ant-space-item'][1]"))
        self.click((self.searches[2]))
        body_text = self.get_text((By.XPATH, "//span[@class='text-lg text-gray-600 font-DanaFanumMedium']"))
        self.click((By.CSS_SELECTOR, ".justify-between > svg"))
        if body_text == "جستجو با کد ملک (مشاهده ملک ثبت شده از طریق کد ملک)":
            return True

    def search_in_map(self):
        self.click((By.XPATH, "//div[@class='hover:text-red-600 cursor-pointer']"))
        try:
            self.wait_until_visible((By.XPATH, "//div[@class='leaflet-top leaflet-left']"))
            return True
        except:
            return False

    def add_property(self):
        self.click((By.LINK_TEXT, u"ثبت ملک"))
        body_text = self.get_text((By.XPATH, "//span[@class='text-gray-600 text-[18px] font-semibold']"))
        self.click((By.XPATH, "//a[@class='text-sm font-semibold text-primary-100 transition']"))
        return body_text

    def add_request(self):
        self.click((By.LINK_TEXT, u"تقاضای ملک"))
        body_text = self.get_text((By.XPATH, "//label[@class='text-[13px]']"))
        self.click((By.XPATH, "//a[@class='text-sm font-semibold text-primary-100 transition']"))
        return body_text

    def employment(self):
        self.click((By.PARTIAL_LINK_TEXT, "فرصت های شغلی"))
        body_text = self.get_text((By.XPATH, "//span[@class='relative']"))
        return body_text