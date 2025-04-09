from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "input.ant-input.ant-input-lg.css-1f3ldtq")
    PASSWORD = (By.CSS_SELECTOR, "input.ant-input.ant-input-lg.css-1f3ldtq.ant-input-outlined.text-center")
    DASHBOARD_BUTTON = (By.XPATH,
                        "/html[@class='font-ShabnamRegular']/body/div[@class='w-full h-fit bg-white relative lg:border border-gray-50 z-[999] lg:shadow-none shadow-[0_4px_6px_-1px_rgba(0,0,0,0.1)]']/div[@class='mx-auto max-w-7xl  px-3 lg:px-0 ']/nav[@class='w-full bg-white ']/div[@class='w-full bg-white flex items-center justify-between py-2']/div[@class='flex items-center gap-3'][2]/button[@class='ant-btn css-1f3ldtq ant-btn-round ant-btn-text ant-btn-color-default ant-btn-variant-text ant-btn-rtl bg-white border text-sm text-gray-500 border-gray-200 px-6 py-1 rounded-2xl hidden lg:flex']")
    USER_BUTTON = (By.XPATH,
                   "/html[@class='font-ShabnamRegular']/body/div[3]/div[@class='ant-dropdown css-1f3ldtq ant-dropdown-rtl ant-dropdown-placement-bottom']/ul[@class='ant-dropdown-menu ant-dropdown-menu-root ant-dropdown-menu-vertical ant-dropdown-menu-light ant-dropdown-menu-rtl css-1f3ldtq']/li[@class='ant-dropdown-menu-item ant-dropdown-menu-item-active ant-dropdown-menu-item-only-child']/span[@class='ant-dropdown-menu-title-content']/a[@class='flex items-center gap-2']")


    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)


