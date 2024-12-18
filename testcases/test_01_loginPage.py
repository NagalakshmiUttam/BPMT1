from pageobjects.login_page import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import time
from allure_commons.types import AttachmentType

import allure

class TestLogin():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    email=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    
    def test_login(self, setup):
        self.logger.info("*** starting test_001_login***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp=LoginPage(self.driver)
        lp.setEmail(self.email)
        lp.setPW(self.password)
        lp.clickLogin()
        time.sleep(2)


        targetText=lp.isTextExists()
        if targetText==True:
            assert True
        else:
            self.driver.save_screenshot("C:\\Nagalakshmi\\PythonPractice\\BPMT\\screenshots\\test_001_failed.png")
            #code to take screen shot

            allure.attach(self.driver.get_screenshot_as_png(), name="failedTC_Screenshot", attachment_type=AttachmentType.PNG)
            assert False

        # self.driver.close()
        self.logger.info("***End of the test_001_login***")
           
        
        # return DashboardPage(self.driver) 