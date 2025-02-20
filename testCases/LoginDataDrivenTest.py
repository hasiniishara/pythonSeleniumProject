import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_002_DDTLogin:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********* Test Login DDT **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginP = LoginPage(self.driver)

        self.rows= ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows", self.rows)

        for r in range(2,self.rows+1):
            self.user=ExcelUtils.readData(self.path, 'Sheet1', r,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1',r,2)
            self.exp_status = ExcelUtils.readData(self.path,'Sheet1',r,3)

            if not self.user or not self.password:
                self.logger.warning(f"Skipping row {r} due to missing data")
                continue

            print(f"Test Data - User: {self.user}, Password: {self.password}, Expected: {self.exp_status}")

            self.loginP.setUserName(self.user)

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

