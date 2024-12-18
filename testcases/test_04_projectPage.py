from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time
from  utilities import XLUtils
from utilities.common_login import CommonLogin
from pageobjects.dashboard_page import DashboardPage
from pageobjects.project_page import ProjectPage
class TestKanban:

    def test_kanban(self,setup):
        logger=LogGen.loggen() 
        logger.info("*** starting test_004_project***")
        
        self.driver=setup
        cmnlogin=CommonLogin(self.driver)
        cmnlogin.common_login()
        # self.driver.refresh()

        dp=DashboardPage(self.driver)
        dp.click_language()
        dp.click_english()
        time.sleep(1)
        dp.click_project_leftside()
        
        pp=ProjectPage(self.driver)
        time.sleep(3)
        # pp.project_table_headings()
        # pp.headline_projects()
        # pp.menu_icon()
        # pp.click_btn_next()
        # pp.click_btn_back()
        # pp.click_btn_backArrow()
        # pp.click_btn_forwardArrow()
        # pp.click_dd_pages_4ele()
        
        pp.click_addProject()
        # pp.sendkeys_projName()
        # pp.sendkeys_startDate()
        # pp.sendkeys_endDate()
        # pp.select_rbtn_internal()
        # pp.select_rbtn_onEffort()
        # pp.dd_select_customer()
        # pp.dd_project_lead()
        # pp.dd_account_manager()
        # pp.sk_proj_summary()
        # pp.click_submit_cr_proj()
        # pp.assert_empty_proj_name_msg()
        # pp.assert_empty_customer_msg()
        # pp.assert_empty_projlead_msg()
        # pp.assert_empty_contact_list_msg()
        # pp.assert_proj_cr_success_msg()
        # pp.assert_proj_del_success_msg()
        # pp.assert_projlead_with_projemp()

        # # pp.sendkeys_search_bar()

        # pp.click_3dots()
        # pp.click_3dots_delete()
        # pp.click_3dots_delCancel()
        # pp.click_3dots_del_del()

        # pp.click_addCustomer()
        # pp.sk_customer_company()
        # pp.sk_customer_street()
        # pp.sk_customer_streetNum()
        # pp.sk_customer_zipcode()
        # pp.sk_customer_city()
        # pp.sk_customer_phnNum()
        # pp.sk_customer_website()
        # pp.sk_cust_technology()
        # pp.sk_cust_email()
        # pp.sk_cust_detail()
        # pp.click_country_arrow()
        # pp.sel_france()
        # pp.sel_industry_arrow()
        # pp.click_all_industry()
        # pp.click_respon_arrow()
        # pp.sel_akshata()
        # pp.click_whrFund_arrow()
        # pp.sel_LinkedIn()
        # pp.click_cust_add_btn()

        # pp.click_add_contact_btn()
        # pp.click_add_con_login_btn()
        # pp.click_add_con_inactive_btn()
        # pp.sk_add_con_fname()
        # pp.sk_add_con_lname()
        # pp.sk_add_con_jobrole()
        # pp.sk_add_con_telephone()
        # pp.sk_add_con_mobile()
        # pp.sk_add_con_email()
        # pp.sk_add_con_DOB()
        # pp.sk_add_con_updates()
        # pp.sk_add_con_interest()
        # pp.click_add_con_btnAdd()
        

        
        
        
       
        # pp.click_contents_3dots()
        # pp.click_addMilestone()
       
        # pp.click_3dots_addsprint()
        # pp.assert_sprintPage_heading()
        # pp.send_keys_sprintname()
        # pp.btn_addFooter_sprint_3dots()
        # pp.assert_empty_sprint_errMsg()
        # pp.assert_BV_sprint_errMsg()
        # pp.assert_repeatSprint_errMsg()
        # pp.assert_start_dt_sprint()
        # pp.assert_end_dt_sprint()
        # pp.sendkeys_description()
        # pp.dd_arrow_sprint()
       
       
       
    


