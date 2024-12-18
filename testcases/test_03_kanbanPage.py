from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import time
from pageobjects.kanban_page import KanbanPage
from pageobjects.login_page import LoginPage
from  utilities import XLUtils
from utilities.common_login import CommonLogin
from pageobjects.dashboard_page import DashboardPage



class TestKanban:

    def test_kanban(self,setup):
        logger=LogGen.loggen() 
        logger.info("*** starting test_002_dashboard***")
        
        self.driver=setup
        cmnlogin=CommonLogin(self.driver)
        cmnlogin.common_login()
        self.driver.refresh()

        dp=DashboardPage(self.driver)
        dp.click_language()
        dp.click_english()
        dp.click_kanban_fullview()

        kp=KanbanPage(self.driver)
        kp.drag_drop1()
        # kp.drag_drop2()
        # kp.drag_drop3()