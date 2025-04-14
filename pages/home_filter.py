from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Home_filter:
    def __init__(self, driver):
        self.driver = driver
        self.search_btn_xpath = '//div[@class = "ant-space-item" and text() = "جستجوی ملک" ]'
        self.buy_btn_xpath = "(//*[normalize-space(text()) and normalize-space(.)='برای خرید در'])[1]"
        self.min_meter_xpath = "(//input)[1]"
        self.max_meter_xpath = "(//input)[2]"
        self.min_price_xpath = "(//input)[3]"
        self.max_price_xpath = "(//input)[4]"
        self.ok_filter_xpath = "(//button[@type = 'button'])[5]"
        # self.type_dic = {1:'آپارتمان' , 2:'آپارتمان موقعیت اداری' , 3:'مشارکت درساخت',4:"باغ و باغچه",5:"زمین",6:"آپارتمان اداری",7:"صنعتی و زراعی",8:"مجتمع آپارتمانی ، مستغلات",9:"تجاری ، مغازه",10:"خانه - ویلا",11:"خانه ، ویلا ، کلنگی"}

    def open_filter(self , driver):
        self.driver = driver
        self.driver.implicitly_wait(6)
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, self.buy_btn_xpath).click()

    def select_type(self , property_type):
            self.driver.find_element(By.XPATH, f'(//div[@class = "text-gray-900  hover:text-white  bg-gray-50 hover:bg-red-600 flex justify-center items-center border-gray-400  py-4 rounded-lg text-xs cursor-pointer"])[{property_type}]').click()




    def enter_filter(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, "(//input[@class = 'ant-select-selection-search-input'])[1]").send_keys("50" + Keys.ENTER)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, self.max_meter_xpath).send_keys("100" + Keys.ENTER)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, self.min_price_xpath).send_keys("1" + Keys.ENTER)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, self.max_price_xpath).send_keys("15" + Keys.ENTER)
        self.driver.implicitly_wait(3)


    def ok_filter(self):
        self.driver = self.driver.find_element(By.XPATH,self.ok_filter_xpath).click()

    def back_page(self):
        self.driver.back()


