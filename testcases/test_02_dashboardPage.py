from utilities.customLogger import LogGen
import time
from pageobjects.dashboard_page import DashboardPage
from utilities.common_login import CommonLogin

class TestDashboard:

    def test_dashboard(self,setup):
        logger=LogGen.loggen() 
        logger.info("*** starting test_002_dashboard***")
        
        self.driver=setup
        cmnlogin=CommonLogin(self.driver)
        cmnlogin.common_login()
        self.driver.refresh()

        dp=DashboardPage(self.driver)
        dp.German_lang_assert()
        dp.click_language()
        dp.click_english()
        time.sleep(1)
        # dp.click_prof_pic()
        # dp.click_prof_text()
        dp.click_notification_icon()
        dp.ntfn_text_assert()

        dp.markAsRead_text_assert()
        dp.viewAllNtfn_text_assert()
        dp.scroll_NtfnPage()

        dp.menu_icon()
        dp.click_dd_analyse()
        dp.click_dd_close()
        dp.click_cancel_kanAna_dd()
        
        dp.drag_drop1()
    
        dp.Kanban_H1()
        dp.Kanban_subFeatures()
        dp.kanban_fullview_btn()

        dp.department_H2()
        dp.department_date()
        dp.click_department_date()
        # dp.click_month()
        # dp.click_week()
        # dp.click_day()
        dp.department_subFeatures()
        dp.click_Dept_overview_subfeature()

        dp.calender_H1()
        dp.calender_sub_features()

        dp.click_kanban_fullview()
        dp.click_dashboard_pagelink()
       
        dp.click_calender_fullview()
        dp.click_dashboard_pagelink()
        
        # dp.click_actualLink_dept()
        # dp.click_meetingsLink_dept()
        # dp.click_RDlink_dept()
        
        dp.scroll_right()
        dp.scrollPage()
        dp.calender_hor_scrollbar()
       
        dp.click_cal_reverseArrow()
        dp.click_cal_forwardArrow()
        dp.version_text()
        dp.company_Nametext()
       
        logger.info("***End of the test_002_dashboard***")