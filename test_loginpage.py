# coding: utf-8

import time

import self as self
from cryptography.hazmat.primitives.twofactor.totp import TOTP
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3.util import wait

from pageObjects.loginpage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen
from testCases.startingBrowser import initiatebrowser

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from pyotp import *
from selenium.webdriver.support import expected_conditions as EC


class Test_1_Login:
    ShopifyBaseURL = ReadConfig.getShopifyURL()
    ShopifyBaseUsername = ReadConfig.getShopifyusername()
    ShopifyBasePassword = ReadConfig.getShopifypassword()

    logger = LogGen.loggen()

    def test1_Shopify_new_Retailer(self, initiatebrowser):
# Login to Shopify
        #self.logger.info("********Login credentials test**********")
        self.driver = initiatebrowser
        self.driver.get(self.ShopifyBaseURL)
        wait_for_loading = self.driver.implicitly_wait(60)
        self.logpageobj = LoginPage(self.driver)
        self.logpageobj.setUsername(self.ShopifyBaseUsername)
        self.driver.maximize_window()
        time.sleep(7)
        self.logpageobj.clicknext()
        time.sleep(7)
        self.logpageobj.setPassword(self.ShopifyBasePassword)
        time.sleep(7)
        self.logpageobj.clickLogin()
        wait_for_loading
        act_title = self.driver.title
        print (act_title)
        if act_title == "Stores - Shopify Partners":
            assert True
            self.logger.info("*******Login credentials test passed*******")
        else:
            self.logger.info("*******Login credentials test failed*******")
            self.driver.save_screenshot(
                '/Users/rasikakuppusamy/PycharmProjects/Cloudshelf_Dev_Env/Screenshots' + 'testtitle.png')
            assert False
        wait_for_loading

# Login to Test Store
        self.driver.find_element_by_xpath("//*[@id='62522228983']").click()
        wait_for_loading
        act_title = self.driver.title
        if act_title == "Production test store - Shopify Partners":
            assert True
        else:
            self.driver.save_screenshot('Screenshots' + 'teststore homepage check.png')
            self.driver.quit()
            assert False
        self.driver.find_element_by_xpath("//*[@id='AppFrameMain']/header/div[1]/div[2]/div/a").click()
        wait_for_loading
        self.driver.switch_to_window(self.driver.window_handles[0])
        wait_for_loading
        self.driver.switch_to_window(self.driver.window_handles[1])
#Add cloudshelf from Shopify store
        time.sleep(2)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver.get("https://apps.shopify.com/cloudshelf")
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@value='Add app']").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'RK')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@placeholder='your-shop-url.myshopify.com']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='your-shop-url.myshopify.com']").send_keys("rasika-teststore2.myshopify.com")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@value='Add app']").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Add sales channel')]")
        # self.driver.find_element_by_xpath("//span[contains(text(),'Add sales channel')]").click()
        # wait_for_loading
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[2])
        time.sleep(2)
        wait_for_loading
        self.driver.find_element_by_xpath("//button[@id='proceed_cta']").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/nav[1]/div[2]/ul[2]/li[3]/div[1]/a[1]/span[1]").click()
#       wait_for_loading
        sync_start_time = time.time()
#         wait_for_loading
#         self.driver.switch_to_window(self.driver.window_handles[0])
#         wait_for_loading
#         self.driver.switch_to_window(self.driver.window_handles[1])
#     #     self.driver.find_element_by_xpath("//*[@id='AppFrameMain']/header/div[1]/div[2]/div/a").click()
#     #     wait_for_loading
#     #     self.driver.switch_to_window(self.driver.window_handles[0])
#     #     wait_for_loading
#     #     self.driver.switch_to_window(self.driver.window_handles[1])
#     #     act_title = self.driver.title
#     #     print (act_title)
#
#     # Import products
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Products')]").click()
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Import')]").click()
#     #     time.sleep(5)
#     #     self.driver.find_element_by_xpath("//input[@id='PolarisDropZone1' or @type='file']").send_keys(
#     #         "/Users/rasikakuppusamy/Downloads/product_template.csv")
#     #     time.sleep(3)
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Upload and continue')]").click()
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Import products')]").click()
#     #     time.sleep(65)
#     #     print "import done"
#
#     # Add Product
#         # self.driver.find_element_by_xpath("//span[contains(text(),'Products')]").click()
#         # wait_for_loading
#         # self.driver.find_element_by_xpath("//span[contains(text(),'Add product')]").click()
#         #
#         # self.driver.find_element_by_css_selector("input").send_keys("PTS sample product1")
#         # wait_for_loading
#         # self.driver.find_element_by_xpath("//option[contains(text(),'Active')]").click()
#         # wait_for_loading
#         # self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
#         # time.sleep(3)
#
#     # Create Collection
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Collections')]").click()
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Create collection')]").click()
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//input[@id='collectionTitleTextField']").send_keys("PTS test collection")
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//option[contains(text(),'Product title')]").click()
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//option[contains(text(),'contains')]").click()
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]").click()
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]").send_keys("example")
#     #     time.sleep(3)
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
#     #     time.sleep(3)
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Products')]").click()
#     #     time.sleep(2)
#     #     self.driver.find_element_by_xpath("//span[contains(text(),'Collections')]").click()
#     #     time.sleep(10)
#     #     self.driver.refresh()
#     #     wait_for_loading
#     #     self.driver.find_element_by_xpath("//input[@id='PolarisTextField10' or @class='Polaris-TextField__Input_30ock Polaris-TextField__Input--hasClearButton_15k6h' and @placeholder='Filter collections']").send_keys("PTS_")
#     #     self.driver.save_screenshot('/Users/rasikakuppusamy/PycharmProjects/Post_production_test/Screenshots' + 't1collections.png')
#     #     print "collections created"
#
# Open cloudshelf manager
        self.driver.execute_script("window.open('');")
        self.driver.switch_to_window(self.driver.window_handles[3])
        self.driver.get("https://manager.cloudshelf.ai/dashboard")
        self.driver.maximize_window()
        self.driver.find_element_by_id('loginBox').send_keys("rasika@cloudshelf.ai")
        self.driver.find_element_by_id('passwordBox').send_keys("wpz8qth2vyr@kbz_XJN")
        self.driver.find_element_by_xpath("//*[@class='authpages_button__2QFfs']").click()
        act_title = self.driver.title
        if act_title == "Cloudshelf Manager":
            assert True
        else:
            self.driver.save_screenshot('Screenshots' + 'teststore homepage check.png')
            self.driver.quit()
            assert False
# time for entering the one time passcode
        wait_for_loading
# # Add new retailer to cloudshelf
# #         Name = "Production test store"
# #         Email = "rasika+teststore4@cloudshelf.ai"
# #         Domain = "rasika-teststore2.myshopify.com"
# #         Password_Shopify_Access_Token = "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"
# #         Shopify_Shared_Secret = "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"
# #         self.driver.find_element_by_xpath("//span[contains(text(),'Retailers')]").click()
# #         wait_for_loading
# #         self.driver.find_element_by_xpath("//span[contains(text(),'New Retailer')]").click()
# #         self.driver.find_element_by_xpath("//input[@name='name']").send_keys(Name)
# #         self.driver.find_element_by_xpath("//input[@name='email']").send_keys(Email)
# #         self.driver.find_element_by_xpath("//input[@name='domain']").send_keys(Domain)
# #         self.driver.find_element_by_xpath("//input[@name='accessToken']").send_keys(Password_Shopify_Access_Token)
# #         self.driver.find_element_by_xpath("//input[@name='sharedSecret']").send_keys(Shopify_Shared_Secret)
# #         time.sleep(2)
# #         self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
# #         wait_for_loading
# Select retailer
        self.driver.find_element_by_xpath("//span[contains(text(),'Retailers')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@id='PolarisTextField1' or @class='Polaris-TextField__Input Polaris-TextField__Input--hasClearButton' and @placeholder='Search']").send_keys("Production test store")
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Production test store')]").click()
        time.sleep(2)
# # # Select cloudshelf and preview
# #         self.driver.find_element_by_xpath("//span[contains(text(),'Cloudshelves')]").click()
# #         wait_for_loading
# #         self.driver.find_element_by_xpath("//span[contains(text(),'Noble test')]").click()
# #         wait_for_loading
#         self.driver.find_element_by_xpath("//span[contains(text(),'Production test store')]")
#
#         self.driver.find_element_by_xpath("//span[contains(text(),'Devices')]").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath("//span[contains(text(),'Retailers Dashboard')]").click()
#         print sync_start_time
#         time.sleep(3)
#         wait_for_loading
#         #self.driver.find_element_by_xpath("//span[contains(text(),'Retailers Dashboard')]").click()
#         #x = self.driver.find_element_by_xpath("//span[@class='Polaris-Badge Polaris-Badge--statusWarning']")
#         # sync_status = self.driver.find_element_by_xpath("//span[@class='Polaris-Badge Polaris-Badge--statusWarning']").text
#         # print sync_status
        sync_status = self.driver.find_element_by_xpath("//span[contains(text(),'Sync')]").text
        print (sync_status)
        if sync_status == "Warning\nSync Pending":
            flag = 1
        else:
            flag = 0
        while flag == 1:
            time.sleep(4)
            sync_status = self.driver.find_element_by_xpath("//span[contains(text(),'Sync')]").text
            if sync_status == "Warning\nSync Pending":
                flag = 1
                continue
            elif sync_status == "Warning\nSyncing Content...":
                flag = 1
                continue
            elif sync_status == "Success\nSync Complete":
                flag = 0
                break
            else:
                flag=0
                break
        print(sync_status)
        sync_end_time = time.time()
        Total_sync_time = sync_end_time-sync_start_time
        print (Total_sync_time)
        self.driver.find_element_by_xpath("//*[@class='Polaris-TopBar-Menu__Activator' and @type = 'button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(),'Sign Out')]").click()
        self.driver.quit()


        # self.driver.find_element_by_xpath("//span[contains(text(),'Cloudshelves')]").click()
        # wait_for_loading
        # self.driver.find_element_by_xpath("//span[contains(text(),'New Cloudshelf')]").click()
        # wait_for_loading
        # self.driver.find_element_by_xpath("//span[contains(text(),'Continue')]").click()
        # wait_for_loading
        # self.driver.find_element_by_xpath("//span[contains(text(),'Preview')]").click()
        # wait_for_loading


# Select retailer
#         self.driver.find_element_by_xpath("//span[contains(text(),'Retailers')]").click()
#         self.driver.find_element_by_xpath("//input[@id='PolarisTextField1' or @class='Polaris-TextField__Input Polaris-TextField__Input--hasClearButton' and @placeholder='Search']").send_keys("Rasika teststore")
#         self.driver.find_element_by_xpath("//span[contains(text(),'Rasika teststore')]").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath("//span[contains(text(),'Cloudshelves')]").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//span[contains(text(),'Noble test')]").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//input[@role='combobox']").send_keys("PTS test collection")
#         wait_for_loading
#         x = self.driver.find_element_by_xpath("//input[@role='combobox']")
#         select_collections = Select(x)
#         time.sleep(3)
#         select_collections.select_by_visible_text("Books")

###### Test 2 #######

    def test2_Shopify_addCollection(self, initiatebrowser):
# Login to Shopify
        #self.logger.info("********Login credentials test**********")
        self.driver = initiatebrowser
        self.driver.get(self.ShopifyBaseURL)
        wait_for_loading = self.driver.implicitly_wait(60)
        self.logpageobj = LoginPage(self.driver)
        self.logpageobj.setUsername(self.ShopifyBaseUsername)
        self.driver.maximize_window()
        time.sleep(7)
        self.logpageobj.clicknext()
        time.sleep(7)
        self.logpageobj.setPassword(self.ShopifyBasePassword)
        time.sleep(7)
        self.logpageobj.clickLogin()
        wait_for_loading
        act_title = self.driver.title
        print (act_title)
        if act_title == "Stores - Shopify Partners":
            assert True
            self.logger.info("*******Login credentials test passed*******")
        else:
            self.logger.info("*******Login credentials test failed*******")
            self.driver.save_screenshot(
                '/Users/rasikakuppusamy/PycharmProjects/Cloudshelf_Dev_Env/Screenshots' + 'testtitle.png')
            assert False
        wait_for_loading

# Login to Test Store
        self.driver.find_element_by_xpath("//*[@id='62522228983']").click()
        wait_for_loading
        act_title = self.driver.title
        if act_title == "Production test store - Shopify Partners":
            assert True
        else:
            self.driver.save_screenshot('Screenshots' + 'teststore homepage check.png')
            self.driver.quit()
            assert False
        self.driver.find_element_by_xpath("//*[@id='AppFrameMain']/header/div[1]/div[2]/div/a").click()
        wait_for_loading
        self.driver.switch_to_window(self.driver.window_handles[0])
        wait_for_loading
        self.driver.switch_to_window(self.driver.window_handles[1])
#Import products
        self.driver.find_element_by_xpath("//span[contains(text(),'Products')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Import')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@id='PolarisDropZone1' or @type='file']").send_keys(
            "/Users/rasikakuppusamy/Downloads/product_template.csv")
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Upload and continue')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Import products')]").click()
        time.sleep(30)
        print ("import done")
#make products available on Cloudshelf
        self.driver.find_element_by_xpath("//span[contains(text(),'More filters')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Availability')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Unavailable on Cloudshelf')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Done')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//thead/tr[1]/th[1]/div[1]/label[1]/span[1]/span[1]/span[1]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'More actions')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Add available channel(s)...')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Make products available')]").click()
        time.sleep(5)
# create collection
        self.driver.find_element_by_xpath("//span[contains(text(),'Products')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Collections')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Create collection')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@id='collectionTitleTextField']").send_keys("Baby products")
        wait_for_loading
        self.driver.find_element_by_xpath("//option[contains(text(),'Product title')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath(
            "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]").click()
        wait_for_loading
        self.driver.find_element_by_xpath(
            "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]").send_keys(
            "baby_hats")
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Products')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(),'Collections')]").click()
        time.sleep(10)
        self.driver.save_screenshot('/Users/rasikakuppusamy/PycharmProjects/Post_production_test/Screenshots' + 'collections.png')
        time.sleep(30)

# # Open cloudshelf manager
        self.driver.execute_script("window.open('');")
        self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver.get("https://manager.cloudshelf.ai/dashboard")
        self.driver.find_element_by_id('loginBox').send_keys("rasika@cloudshelf.ai")
        self.driver.find_element_by_id('passwordBox').send_keys("wpz8qth2vyr@kbz_XJN")
        self.driver.find_element_by_xpath("//*[@class='authpages_button__2QFfs']").click()
        act_title = self.driver.title
        if act_title == "Cloudshelf Manager":
            assert True
        else:
            self.driver.save_screenshot('Screenshots' + 'teststore homepage check.png')
            self.driver.quit()
            assert False
# time for entering the one time passcode
        wait_for_loading
# Select retailer
        self.driver.find_element_by_xpath("//span[contains(text(),'Retailers')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@id='PolarisTextField1' or @class='Polaris-TextField__Input Polaris-TextField__Input--hasClearButton' and @placeholder='Search']").send_keys("Production test store")
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Production test store')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//span[contains(text(),'Cloudshelves')])[2]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'New Cloudshelf')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Continue')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@role='combobox']").send_keys("baby products")
        wait_for_loading
        time.sleep(15)
        self.driver.find_element_by_xpath("//span[contains(text(),'Preview')]").click()
        time.sleep(2)
        Current_url = self.driver.current_url
        print (Current_url)
#Go back to old page
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[3])
        self.driver.maximize_window()

# #Back to preview page
#         self.driver.switch_to_window(self.driver.window_handles[1])
#         time.sleep(2)
#Search for a old product
        self.driver.maximize_window()
        wait_for_loading
        self.driver.find_element_by_xpath("//*[@class='Button Button--medium Button--roundedCorners Button--primary ButtonIcon ButtonIcon--beforeText ButtonIcon__fixed--medium Menu__search']").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@name='NameFilterInput' and @class = 'NameFilterInput__input']").send_keys("baby_hats")
        wait_for_loading
        self.driver.find_element_by_xpath("//*[@class = 'Button Button--large Button--roundedCorners Button--primary FiltersView__footer__searchButton' and @type = 'button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//*[@class='ProductCard__image'])[1]").click()
        time.sleep(2)
        self.driver.save_screenshot('/Users/rasikakuppusamy/PycharmProjects/Post_production_test/Screenshots' + 'collections.png')
        self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver.find_element_by_xpath("//*[@class='Polaris-TopBar-Menu__Activator' and @type = 'button']").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Sign Out')]").click()

# Create new cloudshelf and add new collection to it

###### Test 3 #######

    def test3_Shopify_addProduct(self, initiatebrowser):
# Login to Shopify

# self.logger.info("********Login credentials test**********")
        self.driver = initiatebrowser
        self.driver.get(self.ShopifyBaseURL)
        wait_for_loading = self.driver.implicitly_wait(60)
        self.logpageobj = LoginPage(self.driver)
        self.logpageobj.setUsername(self.ShopifyBaseUsername)
        self.driver.maximize_window()
        time.sleep(7)
        self.logpageobj.clicknext()
        time.sleep(7)
        self.logpageobj.setPassword(self.ShopifyBasePassword)
        time.sleep(7)
        self.logpageobj.clickLogin()
        wait_for_loading
        act_title = self.driver.title
        print (act_title)
        if act_title == "Stores - Shopify Partners":
                assert True
                self.logger.info("*******Login credentials test passed*******")
        else:
                self.logger.info("*******Login credentials test failed*******")
                self.driver.save_screenshot(
                        '/Users/rasikakuppusamy/PycharmProjects/Cloudshelf_Dev_Env/Screenshots' + 'testtitle.png')
                assert False
        wait_for_loading

# Login to Test Store
        self.driver.find_element_by_xpath("//*[@id='62522228983']").click()
        wait_for_loading
        act_title = self.driver.title
        if act_title == "Production test store - Shopify Partners":
                assert True
        else:
                self.driver.save_screenshot('Screenshots' + 'teststore homepage check.png')
                self.driver.quit()
                assert False
        self.driver.find_element_by_xpath("//*[@id='AppFrameMain']/header/div[1]/div[2]/div/a").click()
        wait_for_loading
        self.driver.switch_to_window(self.driver.window_handles[0])
        wait_for_loading
        self.driver.switch_to_window(self.driver.window_handles[1])

# Add a single Product
# Import product
        self.driver.find_element_by_xpath("//span[contains(text(),'Products')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Import')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@id='PolarisDropZone1' or @type='file']").send_keys("/Users/rasikakuppusamy/Downloads/wildswans_final copy.csv")
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Upload and continue')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Import products')]").click()
        time.sleep(10)
        print ("import done")
#make products available on Cloudshelf
        self.driver.find_element_by_xpath("//span[contains(text(),'More filters')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Availability')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Unavailable on Cloudshelf')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Done')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//thead/tr[1]/th[1]/div[1]/label[1]/span[1]/span[1]/span[1]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'More actions')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Add available channel(s)...')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Make products available')]").click()
        time.sleep(5)
#         self.driver.find_element_by_xpath("//span[contains(text(),'Products')]").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//span[contains(text(),'Add product')]").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//*[@name='title' and @placeholder='Short sleeve t-shirt']").send_keys("baby_hats with variants")
#         wait_for_loading
#         self.driver.find_element_by_xpath("//*[@name = 'price']").send_keys("1000")
#         wait_for_loading
#
        #self.driver.find_element_by_xpath("//*[@name='isAddingOptions' and @type='checkbox']").click()
       # wait_for_loading
        #self.driver.find_element_by_xpath("//*[@placeholder='Size']").send_keys("Size")
#         wait_for_loading
#         self.driver.find_element_by_xpath("//*[@placeholder='Medium']").send_keys("0-12months")
#         wait_for_loading
#         self.driver.find_element_by_xpath("//*[@placeholder='Add another value']").send_keys("1-2years")
#         wait_for_loading
#         self.driver.find_element_by_xpath("//option[contains(text(),'Active')]").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
#         time.sleep(3)
# Open cloudshelf manager
        self.driver.execute_script("window.open('');")
        self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver.get("https://manager.cloudshelf.ai/dashboard")
        self.driver.find_element_by_id('loginBox').send_keys("rasika@cloudshelf.ai")
        self.driver.find_element_by_id('passwordBox').send_keys("wpz8qth2vyr@kbz_XJN")
        self.driver.find_element_by_xpath("//*[@class='authpages_button__2QFfs']").click()
        act_title = self.driver.title
        if act_title == "Cloudshelf Manager":
            assert True
        else:
            self.driver.save_screenshot('Screenshots' + 'teststore homepage check.png')
            self.driver.quit()
            assert False
# time for entering the one time passcode
        wait_for_loading
# Select retailer
        self.driver.find_element_by_xpath("//span[contains(text(),'Retailers')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@id='PolarisTextField1' or @class='Polaris-TextField__Input Polaris-TextField__Input--hasClearButton' and @placeholder='Search']").send_keys("Production test store")
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Production test store')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//span[contains(text(),'Cloudshelves')])[2]").click()
        wait_for_loading
# Select cloudshelf and preview
        self.driver.find_element_by_xpath("(//*[@class='Polaris-TextStyle--variationStrong'])[1]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Preview')]").click()
        wait_for_loading
# Check if new attribute added to the cloudshelf
#         self.driver.maximize_window()
#         wait_for_loading
        self.driver.find_element_by_xpath("(//*[@class='ImageCard__title'])[2]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//*[@class='Button Button--medium Button--roundedCorners Button--primary ButtonIcon ButtonIcon--beforeText ButtonIcon__fixed--medium Menu__search']").click()
        wait_for_loading
        self.driver.save_screenshot('/Users/rasikakuppusamy/PycharmProjects/Post_production_test/Screenshots','force_filter.png')
###### Test 4 ######
    def test4_Cloudshelf_preview_searchproducts(self, initiatebrowser):
# Open cloudshelf manager
        #wait_for_loading = self.driver.implicitly_wait(60)
        #self.driver.execute_script("window.open('');")
        #self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver = initiatebrowser
        self.driver.get("https://manager.cloudshelf.ai/dashboard")
        wait_for_loading = self.driver.implicitly_wait(60)
        self.driver.find_element_by_id('loginBox').send_keys("rasika@cloudshelf.ai")
        wait_for_loading
        self.driver.find_element_by_id('passwordBox').send_keys("wpz8qth2vyr@kbz_XJN")
        wait_for_loading
        self.driver.find_element_by_xpath("//*[@class='authpages_button__2QFfs']").click()
        act_title = self.driver.title
        # result = self.driver.find_element_by_xpath("//*[@class='authpages_button__2QFfs']").is_enabled()
        # print result
        act_title = self.driver.title
        if act_title == "Cloudshelf Manager":
            assert True
        else:
            self.driver.save_screenshot('../Screenshots' + 'teststore homepage check.png')
            self.driver.quit()
            assert False
# time for entering the one time passcode
        wait_for_loading
# Select retailer
        self.driver.find_element_by_xpath("//span[contains(text(),'Retailers')]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@id='PolarisTextField1' or @class='Polaris-TextField__Input Polaris-TextField__Input--hasClearButton' and @placeholder='Search']").send_keys("Production test store")
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Production test store')]").click()
        wait_for_loading
# Select cloudshelf and preview
        self.driver.find_element_by_xpath("(//span[contains(text(),'Cloudshelves')])[2]").click()
        wait_for_loading
        self.driver.find_element_by_xpath("(//*[@class='Polaris-TextStyle--variationStrong'])[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Preview')]").click()
        wait_for_loading
#Go back to old page
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(2)
#Back to preview page
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(2)
#Search for a old product
        wait_for_loading
        self.driver.find_element_by_xpath("//*[@class='Button Button--medium Button--roundedCorners Button--primary ButtonIcon ButtonIcon--beforeText ButtonIcon__fixed--medium Menu__search']").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@name='NameFilterInput' and @class = 'NameFilterInput__input']").send_keys("the nordic diet book")
        wait_for_loading
        self.driver.find_element_by_xpath("//*[@class = 'Button Button--large Button--roundedCorners Button--primary FiltersView__footer__searchButton' and @type = 'button']").click()
        time.sleep(5)
        self.driver.save_screenshot('../Screenshots' + 'Old product.png')
#Search for a new product
        self.driver.refresh()
        self.driver.find_element_by_xpath("//*[@class='Button Button--medium Button--roundedCorners Button--primary ButtonIcon ButtonIcon--beforeText ButtonIcon__fixed--medium Menu__search']").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//input[@name='NameFilterInput' and @class = 'NameFilterInput__input']").clear()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='NameFilterInput' and @class = 'NameFilterInput__input']").send_keys("baby_hats with variants")
        wait_for_loading
        self.driver.find_element_by_xpath("//*[@class = 'Button Button--large Button--roundedCorners Button--primary FiltersView__footer__searchButton' and @type = 'button']").click()
        time.sleep(3)
        self.driver.save_screenshot('../Screenshots' + 'New product.png')
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(2)
#Logout from manager
        self.driver.find_element_by_xpath("//*[@class='Polaris-TopBar-Menu__Activator' and @type = 'button']").click()
        wait_for_loading
        self.driver.find_element_by_xpath("//span[contains(text(),'Sign Out')]").click()
        self.driver.quit()

###### Test 5 #######

    def test5_Cloudshelf_Addproduct_and_buy(self, initiatebrowser):
# Open cloudshelf manager
#         self.driver.execute_script("window.open('');")
#         self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver = initiatebrowser
        self.driver.get("https://manager.cloudshelf.ai/dashboard")
        wait_for_loading = self.driver.implicitly_wait(60)
        self.driver.find_element_by_id('loginBox').send_keys("rasika@cloudshelf.ai")
        wait_for_loading
        self.driver.find_element_by_id('passwordBox').send_keys("wpz8qth2vyr@kbz_XJN")
        wait_for_loading
        self.driver.find_element_by_xpath("//*[@class='authpages_button__2QFfs']").click()
        act_title = self.driver.title
        if act_title == "Cloudshelf Manager":
            assert True
        else:
            self.driver.save_screenshot('../Screenshots' + 'teststore homepage check.png')
            self.driver.quit()
            assert False
# time for entering the one time passcode
        wait_for_loading
        self.driver.find_element_by_xpath("(//input[@class='pairing_code_input__22abR'])[1]")
        #authField = self.driver.find_elements_by_xpath("(//input[@class='pairing_code_input__22abR'])[1]")
        wait_for_loading
        totp = TOTP("4I724MYWCHDYPJKOU36FXZMWNLQWOYVE")
        token = totp.now()
        print (token)
# enter the token in the UI
        self.driver.find_element_by_xpath("(//input[@class='pairing_code_input__22abR'])[1]").click()
        self.driver.find_element_by_xpath("(//input[@class='pairing_code_input__22abR'])[1]").send_keys(token)
# click on the button to complete 2FA
        self.driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
# Select retailer
#         self.driver.find_element_by_xpath("//span[contains(text(),'Retailers')]").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//input[@id='PolarisTextField1' or @class='Polaris-TextField__Input Polaris-TextField__Input--hasClearButton' and @placeholder='Search']").send_keys("Production test store")
#         wait_for_loading
#         self.driver.find_element_by_xpath("//span[contains(text(),'Production test store')]").click()
#         time.sleep(2)
# #Go to devices
#         self.driver.find_element_by_xpath("//span[contains(text(),'Devices')]").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//span[contains(text(),'Pair Device')]").click()
#         wait_for_loading
#         self.driver.execute_script("window.open('');")
#         self.driver.switch_to_window(self.driver.window_handles[1])
#         wait_for_loading
#         self.driver.get("https://device.cloudshelf.app/new")
#         wait_for_loading
#         # self.driver.find_element_by_xpath("//button[contains(text(),'Set up device again')]").click()
#         # wait_for_loading
#         device_code = self.driver.find_element_by_xpath("//*[@class='deviceCode']").text
#         print device_code
#         time.sleep(3)
#         self.driver.switch_to_window(self.driver.window_handles[0])
#         self.driver.maximize_window()
#         self.driver.refresh()
#         time.sleep(3)
#         self.driver.find_element_by_xpath("//*[1][@class='pairing_code_input__22abR']").send_keys(device_code)
#         time.sleep(3)
#         self.driver.find_element_by_xpath("//span[contains(text(),'Continue')]").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath("(//span[contains(text(),'Cloudshelf')])").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//*[@class='Polaris-Select__Input']").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("(//span[contains(text(),'2022')])[1]")
#         wait_for_loading
#         self.driver.switch_to_window(self.driver.window_handles[1])
# # Search for products in cloudshelf device
#         wait_for_loading
#         self.driver.find_element_by_xpath("//*[@class='Button Button--medium Button--roundedCorners Button--primary ButtonIcon ButtonIcon--beforeText ButtonIcon__fixed--medium Menu__search']").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//input[@name='NameFilterInput' and @class = 'NameFilterInput__input']").send_keys("the nordic diet book")
#         wait_for_loading
#         self.driver.find_element_by_xpath("//*[@class = 'Button Button--large Button--roundedCorners Button--primary FiltersView__footer__searchButton' and @type = 'button']").click()
#         time.sleep(4)
#         self.driver.find_element_by_xpath("(//*[@class='ProductCard__image'])[1]").click()
#         time.sleep(2)
#         # self.driver.find_element_by_xpath("//input[@id='Black_']").click()
#         # time.sleep(2)
#         # self.driver.find_element_by_xpath("(//*[@class='ButtonSelectable ProductVariantOptions__option'])[1]").click()
#         # time.sleep(2)
#         self.driver.find_element_by_xpath("//span[contains(text(),'Add to basket')]").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("(//*[@class='Button Button--medium Button--roundedCorners Button--none ButtonIcon ButtonIcon--beforeText ButtonIcon__fixed--medium Menu__backButton '])").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("(//*[@class='Button Button--medium Button--roundedCorners Button--primary ButtonIcon ButtonIcon--beforeText ButtonIcon__fixed--medium Menu__search'])").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//input[@name='NameFilterInput' and @class = 'NameFilterInput__input']").clear()
#         time.sleep(2)
#         self.driver.find_element_by_xpath("//input[@name='NameFilterInput' and @class = 'NameFilterInput__input']").send_keys("baby_hats with variant")
#         time.sleep(4)
#         self.driver.find_element_by_xpath("//*[@class = 'Button Button--large Button--roundedCorners Button--primary FiltersView__footer__searchButton' and @type = 'button']").click()
#         time.sleep(3)
#         self.driver.find_element_by_xpath("(//*[@class='ProductCard__image'])[1]").click()
#         time.sleep(2)
#         # self.driver.find_element_by_xpath("//span[contains(text(),'Add to basket')]").click()
#         # wait_for_loading
#         # self.driver.find_element_by_xpath("//input[@id='S_']").click()
#         # time.sleep(2)
#         # self.driver.find_element_by_xpath("(//*[@class='ButtonSelectable ProductVariantOptions__option'])[1]").click()
#         # time.sleep(2)
#         self.driver.find_element_by_xpath("//span[contains(text(),'Add to basket')]").click()
#         time.sleep(3)
#         self.driver.find_element_by_xpath("//*[@class='Button Button--medium Button--roundedCorners Button--primary ButtonIcon ButtonIcon--beforeText ButtonIcon__fixed--medium ']").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//button[contains(text(),'Checkout with your phone')]").click()
#         time.sleep(5)
#         QR = self.driver.find_element_by_xpath("//p[@class='PurchaseView__helpText']").text
#         if QR =="Scan code with your phone's camera or QR reader":
#             print "QR code is displayed. Scan to buy"
#         else:
#             print "No QR code displayed"
#         self.driver.save_screenshot('../Screenshots' + 'QR_Code.png')
#         time.sleep(2)
#         self.driver.switch_to_window(self.driver.window_handles[0])
#         time.sleep(2)
# #Logout from manager
#         self.driver.find_element_by_xpath("//*[@class='Polaris-TopBar-Menu__Activator' and @type = 'button']").click()
#         wait_for_loading
#         self.driver.find_element_by_xpath("//span[contains(text(),'Sign Out')]").click()
#         self.driver.quit()






















        #Check if collection is created
        # self.driver.find_element_by_xpath("//*[@class='Polaris-TextField__Input_30ock Polaris-TextField__Input--hasClearButton_15k6h']").send_keys("PTS sample product1")
        # wait_for_loading
        # self.driver.find_element_by_xpath("//span[contains(text(),'Import')]").click()
        # self.driver.implicitly_wait(3)
        # self.driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[3]/div[118]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/span[1]/input[1]").click()

        #send_keys("/Users/rasikakuppusamy/Documents/testproducts.xlsx")

        #self.driver.find_element_by_xpath("//*[@class='Polaris-TopBar-Menu__Activator_e3w0d']").click()


