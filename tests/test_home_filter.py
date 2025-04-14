from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from Pages.home_filter import Home_filter
from time import sleep


class Test_home_filter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://deltadev.ir/tehran")
        self.filter = Home_filter(driver = self.driver)
        self.type_dic = {1:'آپارتمان' , 2:'آپارتمان موقعیت اداری' , 3:'مشارکت درساخت',4:"باغ و باغچه",5:"زمین",6:"آپارتمان اداری",7:"صنعتی و زراعی",8:"مجتمع آپارتمانی ، مستغلات",9:"تجاری ، مغازه",10:"خانه - ویلا",11:"خانه ، ویلا ، کلنگی"}


    def test_Use_filter(self):

            sleep(5)

            for keys , value in self.type_dic.items():

                self.filter.open_filter(self.driver)
                self.driver.implicitly_wait(5)
                self.filter.select_type(keys)
                print(value)
                self.driver.implicitly_wait(6)
                self.filter.enter_filter()
                self.driver.implicitly_wait(6)
                input_value = self.verify_filter_values()
                self.driver.implicitly_wait(6)
                if input_value != [0,0,0,0]:
                    self.filter.ok_filter()
                    sleep(5)
                    self.verify_buy_page_filter(value)
                    self.verify_prop_details(input_value)
                    self.driver.implicitly_wait(6)
                    print()
                else:
                    print("فیلتر مشکل دارد")
                print("****************************************")

                sleep(5)

                self.driver.execute_script("window.location = 'https://deltadev.ir/tehran';")
                sleep(5)
            # except:
            #     print("در استفاده از فیلتر مشکل به وجود اومده")

    def verify_prop_details(self, details):
        min_price = details[2]
        max_price = details[3]
        min_meter = details[1]
        max_meter = details[0]


        try:
            prop_count = self.driver.find_element(By.XPATH , "(//span[@class = 'text-primary-100'])[2]").text
            prop_count = prop_count.split()
            prop_count = int(prop_count[0])
            count = min(prop_count,8)
            if count != 0 :
                    for i in range(1,count):

                        find_price = self.driver.find_element(By.XPATH , f'(//div[@class = "flex flex-col gap-1 "]/div[1]/span[@class = "font-DanaFanumMedium text-sm"])[{i}]').text
                        find_price = find_price.replace("," , "")
                        find_price = int(find_price)
                        assert find_price >= min_price and find_price<= max_price , (f" خروجی قیمت مطابق فیلتر اعمال شده نیست")
                        find_meter = self.driver.find_element(By.XPATH , f'(//div[@class = "flex flex-wrap text-[10px] md:text-xs items-start lg:text-[14px] gap-1 md:gap-2 "]/div[2])[{i}]').text
                        find_meter = find_meter.split()
                        find_meter = find_meter[1]
                        find_meter = int(find_meter)
                        assert find_meter>=min_meter and find_price>=max_meter , (f" خروجی قیمت مطابق فیلتر اعمال شده نیست")

            else:
                print("آگهیی یافت نشد")
        except AssertionError as e:
            print(e)





    def verify_buy_page_filter(self , prop):
        # title_page=self.buy.find_header().text()
        title_page = self.driver.find_element(By.XPATH , "//h1[@class = 'text-sm font-bold']").text
        type_transaction = self.driver.find_element(By.XPATH , "//span[@class = 'ant-select-selection-item' and @title='خرید']").text
        type_prop = self.driver.find_element(By.XPATH,
                                             f"//span[@class = 'ant-select-selection-item' and @title='{prop}']").text
        try:

            assert  prop in title_page , (f"صفحه مورد نظر خرید نیست")
            assert type_transaction == "خرید" , ("type of transaction is not {}")
            assert type_prop == prop , (f"the type of property: {prop} but is show {type_prop}")

        except AssertionError as e:
            print(f"Assertion Error: {e}")


    def verify_filter_values(self):
        sleep(5)
        first_input = self.driver.find_element(By.XPATH,"(//div[@class = 'ant-select-selector'])[1]").text
        second_input = self.driver.find_element(By.XPATH,"(//div[@class = 'ant-select-selector'])[2]").text
        third_input = self.driver.find_element(By.XPATH,"(//div[@class = 'ant-select-selector'])[3]").text
        fourth_input = self.driver.find_element(By.XPATH,"(//div[@class = 'ant-select-selector'])[4]").text



        expected_values = {
                1: "50",
                2: "100",
                3: "1",
                4: "15"
            }

        list_input = []


        # try:
        # assert expected_values[1] in first_input , (f"input value is not {first_input}")
        if first_input =="متراژ از":
            list_input.append(0)
            print("فیلتر بخش((متراژ از )) خراب است")
        else:
            first_meter = first_input.split()
            num_1 = int(first_meter[0])
            list_input.append(num_1)



        # assert expected_values[2] in second_input, (f"input value is not {second_input}")
        if second_input =="متراژ تا":
            list_input.append(0)
            print("فیلتر بخش((متراژ تا )) خراب است")
        else:
            second_meter = second_input.split()
            num_2 = int(second_meter[0])
            list_input.append(num_2)



        # assert expected_values[3] in third_input, (f"input value is not {third_input}")
        if third_input =="حداقل قیمت":
            list_input.append(0)
            print("فیلتر بخش((حداقل قیمت )) خراب است")
        else:
            first_price = third_input.split()
            num_3 = int(first_price[0])*1000000000
            list_input.append(num_3)



        # assert expected_values[4] in fourth_input, (f"input value is not {fourth_input}")
        if fourth_input =="حداکثر قیمت":
            list_input.append(0)
            print("فیلتر بخش((حداکثر قیمت )) خراب است")
        else:
            second_price = fourth_input.split()
            num_4 = int(second_price[0]) * 1000000000
            list_input.append(num_4)



        return list_input

        # except AssertionError as e:
        #     print(f"Assertion Error: {e}")















        # values = self.driver.find_elements(By.XPATH, "//span[@class='ant-select-selection-item']")
        # expected_values = {
        #     1: "50",
        #     2: "100",
        #     3: "1",
        #     4: "15"
        # }
        # list_input = []
        #
        # for value in range(1, len(values) + 1):
        #     input_text = self.driver.find_element(
        #         By.XPATH, f"(//span[@class='ant-select-selection-item'])[{value}]"
        #     ).text
        #     null_input = self.driver.find_element(By.XPATH , "//span[@class='ant-select-selection-placeholder']")
        #     print(input_text)
        #     if not input_text:
        #         list_input.append(0)
        #     list_input.append(input_text)
        #
        #     print(f"مقدار انتظاری برای property {value}: {expected_values[value]}")
        #     print(f"مقدار واقعی در صفحه: {input_text}")
        #     try:
        #         assert expected_values[value] in input_text ,(
        #     f"عدم تطابق در property {value}: "
        #     f"انتظار '{expected_values[value]}'، اما دریافت '{input_text}'"
        # )
        #         print(f"✓ Property {value} صحیح است\n")
        #     except AssertionError as e:
        #         print(f"Assertion Error: {e}")
        #
        # return list_input

    def tearDown(self):
        self.driver.quit()

