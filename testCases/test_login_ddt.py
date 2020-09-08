from pageObjects.loginPages import login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils
import time
"""
How to run test:
pytest -v -s testCases/test_login.py --browser chrome (or firefox)
"""
class Test_002_DDT_login:
    baseURL = ReadConfig.getApplicationURL()
    path = "./nopcommerceApp/TestData/testdata.xlsx"

    logger = logGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("**** Test_002_DDT_login ****")
        self.logger.info("**** Verifying Login DDT test ****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=login(self.driver)
        self.rows = XLUtils.getColumnCount(self.path,"Sheet1")
        print(f'Number of Rows in a Excel, {self.rows}')
        lst_status = []  #empty list variable
        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path,'Sheet1', r, 2)

            self.exp = XLUtils.readData(self.path,'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("The test Passed")
                    lst_status.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.info("The test Failed")
                    #self.lp.clickLogout()
                    lst_status.append('Fail')
                self.lp.clickLogout()
            else:
                if self.exp == 'Pass':
                    self.logger.info("*** The test Failed ***")
                    lst_status.append('Fail')
                elif self.exp == 'Fail':
                    self.logger.info("*** The test Passed ***")
                    #self.lp.clickLogout()
                    lst_status.append('Pass')
                self.lp.clickLogout()


        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test passed ****")
            assert True
        else:
            self.logger.error("**** Login DDT test failed ****")
            assert False
        self.logger.error("**** Login DDT test completed ****")
        self.driver.close()
