import pytest
from utilities.readProperties import ReadConfig
from pageObjects.loginPages import login
from utilities.customLogger import logGen
"""
How to run test:
pytest -v -s testCases/test_login.py --browser chrome (or firefox)
"""
class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self, setup):
        self.logger.info("**** Test_001_login ****")
        self.logger.info("**** Verifying Home title page ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("**** homepageTitle passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot("./nopcommerceApp/Screenshots/" + "test_homepageTitle.png")
            self.logger.error("**** homepageTitle failed ****")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
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
        if act_title == "Dashboard / nopCommerce administration123":
            assert True
            self.logger.info("**** Login test passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "./nopcommerceApp/Screenshots/test_login.png")
            self.logger.error("**** homepageTitle failed ****")
            self.logger.error("**** Login test failed ****")
            self.driver.close()
            assert False
