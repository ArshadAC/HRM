import time

import allure
import pytest
from pageObjects.LoginPage import loginPage
from utilities.readProperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login:
    Url = Readconfig.getURL()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_Page_Title_001(self, setup):

        self.driver = setup
        self.log.info("test_Page_Title_001 started")
        self.log.info("opening browser and naviagting to Url")
        self.driver.get(self.Url)
        # self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        if self.driver.title == "OrangeHRM":
            self.log.info("test_Page_Title_001 is Passed")
            self.log.info("Page Title is-->" + self.driver.title)
            assert True
            print(self.driver.current_window_handle)
        else:
            self.log.info("test_Page_Title_001 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_Page_Title_001 is completed")

    @pytest.mark.regression
    @allure.title("Add User Test Case")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.story("Customer")
    @allure.severity("High")
    def test_login_002(self, setup):
        self.driver = setup
        self.log.info("test_login_002 is started")
        self.log.info("Opening Browser and Navigating to Url")
        self.driver.get(self.Url)
        # self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # driver = webdriver.Firefox()
        # self.driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        self.lp = loginPage(self.driver)
        self.log.info("Entering username-->" + self.Username)
        self.lp.Enter_UserName(self.Username)
        # self.lp.Enter_UserName("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.log.info("Entering Password -->" + self.Password)
        self.lp.Enter_Password(self.Password)
        # self.lp.Enter_Password("admin123")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.log.info("Click on Login Button")
        self.lp.Click_Login()
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # time.sleep(5)
        if self.lp.Login_Status() == True:
            print("Test Passed")
            self.driver.save_screenshot("E:\\Automation Project\\OrangeHRM\\Screenshots\\test_login_pass.png")
            self.log.info("Click on Menu Button ")
            self.lp.Click_Menu_Button()
            self.log.info("Click on Logout Button")
            self.lp.Click_Logout()
            assert True
        else:
            print("Test Failed")
            assert False

        self.driver.close()
        self.log.info("test_login_002 is completed")

