from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "txtUsername"
    textbox_userpassword_id = "txtPassword"
    button_login_xpath = "//*[@id=\"frmLogin\"]/div[4]/button"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setUserPassword(self,userpassword):
        self.driver.find_element(By.ID,self.textbox_userpassword_id).clear()
        self.driver.find_element(By.ID,self.textbox_userpassword_id).send_keys(userpassword)

    def userLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()