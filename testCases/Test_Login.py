import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserNAME()
    password = ReadConfig.getUserPW()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("********* Test Login **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginP = LoginPage(self.driver)
        self.loginP.setUserName(self.username)
        self.loginP.setUserPassword(self.password)
        self.loginP.userLogin()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Employee Management":
            assert True
            self.driver.close()
            self.logger.info("********* Test Login test case is passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********* Test Login test case is failed **********")
            assert False

