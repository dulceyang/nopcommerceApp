import pytest
from selenium import webdriver
from pageObjects.loginPages import login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
"""
How to run test:
pytest -v -s testCases/test_login.py --browser chrome (or firefox)
"""
class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()

    def test_homepageTitle(self, setup):
        self.logger.info("**** Test_001_login ****")
        self.logger.info("**** Verifying Home title page ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("**** homepageTitle passed ****")
        else:
            self.driver.save_screenshot("./Screenshots/test_homepageTitle")
            self.logger.error("**** homepageTitle failed ****")
            assert False
        self.driver.close()


    def test_login(self, setup):
        self.logger.info("**** Test_002_login ****")
        self.logger.info("**** Verifying Login test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**** Login test passed ****")
        else:
            assert False
            self.logger.error("**** Login test failed ****")
        self.driver.close()
