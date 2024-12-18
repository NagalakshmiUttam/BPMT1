from utilities import XLUtils
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.locators import LocatorsProjectPage
from pageobjects.locators import LocatorsDashboardPage
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure


class ProjectPage():

    path=r"C:\Nagalakshmi\PythonPractice\BPMT admin_login\testdata\pythonSelDemo.xlsx"

    def __init__(self,driver):
        self.driver=driver

    def project_table_headings(self):
        list_data1=[]
        fourteen_elements= WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(LocatorsProjectPage.project_table_headings))
        text_of_14ele = fourteen_elements.text
        all_elements_in_list = text_of_14ele.replace("\n",",").split(",")

        for r in range(4,18):
            data1=XLUtils.readData(self.path,"Project_page",r,1)
            list_data1.append(data1)
        print(len(list_data1))

        for i in range(0,len(all_elements_in_list)): #we can take len(list_data1), result will be same because both the length is equal to 14.
            for t in range(4,18):
                if list_data1[i]==all_elements_in_list[i]:
                    XLUtils.writeData(self.path,"Project_page",t,4,"pass")
                    XLUtils.fillGreenColor(self.path,"Project_page",t,4)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Project_page",t,4,"failed")
                    XLUtils.fillRedColor(self.path,"Project_page",t,4)
                    assert False
                    
    def headline_projects(self):
        txt_proj=XLUtils.readData(self.path,"Project_page",3,1)
        print(txt_proj)
        webElement=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LocatorsProjectPage.assert_headline_project)).text
        print(webElement)
        if webElement == txt_proj:
            XLUtils.writeData(self.path,"Project_page",3,4,"pass")
            XLUtils.fillGreenColor(self.path,"Project_page",3,4)
            assert True
        else:
            XLUtils.writeData(self.path,"Project_page",3,4,"failed")
            XLUtils.fillRedColor(self.path,"Project_page",3,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="projects_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def menu_icon(self):
        for i in range(0,2):
            if i<2:
                menu=self.driver.find_element(*LocatorsDashboardPage.img_menuIcon_x)
                self.driver.execute_script("arguments[0].click();", menu)
                time.sleep(2)

    def sendkeys_search_bar(self):
        search_name=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsProjectPage.search_bar))
        search_name.send_keys("uttam24")
        # self.driver.refresh()
        time.sleep(1)
        # search_name.clear()
        
    def click_btn_next(self):
         for i in range(0,20):
            if i<23:
                next=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_next_x))
                self.driver.execute_script("arguments[0].click();", next)
                if (self.driver.find_element(*LocatorsProjectPage.after_click_next)).is_displayed:
                    assert True
                time.sleep(1)

    def click_btn_back(self):
        for i in range(0,19):
            if i<22:
                back=self.driver.find_element(*LocatorsProjectPage.btn_back_x)
                self.driver.execute_script("arguments[0].click();", back)
                if (self.driver.find_element(*LocatorsProjectPage.after_click_back)).is_displayed:
                    assert True
                time.sleep(1)

    def click_btn_backArrow(self):
        back_arrow=self.driver.find_element(*LocatorsProjectPage.btn_back_arrow)
        self.driver.execute_script("arguments[0].click();", back_arrow)
        time.sleep(2)

    def click_btn_forwardArrow(self):
        forward_arrow=self.driver.find_element(*LocatorsProjectPage.btn_forward_arrow)
        self.driver.execute_script("arguments[0].click();", forward_arrow)
        time.sleep(2)
    
    def click_dd_pages(self):
        pagination=WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(LocatorsProjectPage.dd_pages))
        ActionChains(self.driver).move_to_element(pagination).click().perform()
        # self.driver.execute_script("arguments[0].click();", pagination)

    def click_dd_pages_4ele(self):
        self.click_dd_pages()
        all_elements=WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(LocatorsProjectPage.dd_pages_4ele))
        for i in range(len(all_elements)):
            all_elements=WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(LocatorsProjectPage.dd_pages_4ele))
            all_elements[i].click()
            time.sleep(2)
            if i < len(all_elements)-1:
                self.click_dd_pages()
                time.sleep(1)

    # =========================================================> "Create Project" <===========================================================================
    def click_addProject(self):
        addProj=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_addProject_x))
        self.driver.execute_script("arguments[0].click();", addProj)

    def sendkeys_projName(self):
        projName=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.txt_projName_x))
        projName.send_keys("uttam24")
        time.sleep(1)

    def sendkeys_startDate(self):
        startDate=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.txt_startDate_x))
        startDate.clear()
        startDate.send_keys("01.11.2022")
        
    def sendkeys_endDate(self):
        endDate=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.txt_endDate_x))
        endDate.send_keys("07.08.2023")

    def select_rbtn_internal(self):
        rbtn1=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.rbtn_internal_x))
        self.driver.execute_script("arguments[0].click();", rbtn1)

    def select_rbtn_onEffort(self):
        rbtn1=WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(LocatorsProjectPage.rbtn_onEffort_x))
        self.driver.execute_script("arguments[0].click();", rbtn1)
        time.sleep(2)

    def dd_select_customer(self):
        time.sleep(5)
        sel_cust=WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(LocatorsProjectPage.dd_customers_x))
        sel_cust.click()
        sel_cust_drop=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.dd_sel_customer))
        sel_cust_drop.click()
        time.sleep(3)

    def dd_project_lead(self):
        time.sleep(5)
        sel_pl=WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(LocatorsProjectPage.dd_project_lead))
        time.sleep(2)
        sel_pl.click()
        sel_pl_from_dd=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.dd_sel_akash))
        sel_pl_from_dd.click()

    def dd_account_manager(self):
        time.sleep(5)
        sel_acc_manager=WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(LocatorsProjectPage.dd_account_manager))
        sel_acc_manager.click()
        sel_am_from_dd=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.dd_sel_adithi))
        sel_am_from_dd.click()

    def sk_proj_summary(self):
        proj_summary=WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(LocatorsProjectPage.txt_proj_summary))
        ActionChains(self.driver).move_to_element(proj_summary).click().perform()
        proj_summary.send_keys("HRM based application")

    def click_submit_cr_proj(self):
        time.sleep(5)
        click_submit=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.btn_submit_cre_proj))
        click_submit.click()

    def assert_empty_proj_name_msg(self):
        self.click_submit_cr_proj()
        assert_empty_proj_name=self.driver.find_element(*LocatorsProjectPage.assert_empty_proj_name)
        if assert_empty_proj_name=="Project Name is required":
            assert True
        time.sleep(1)

    def assert_empty_customer_msg(self):
        self.click_submit_cr_proj()
        assert_empty_cust_errmsg=self.driver.find_element(*LocatorsProjectPage.assert_empty_cust_errmsg)
        if assert_empty_cust_errmsg=="Customer is required":
            assert True
        time.sleep(1)

    def assert_empty_projlead_msg(self):
        self.click_submit_cr_proj()
        assert_empty_projlead_errmsg=self.driver.find_element(*LocatorsProjectPage.assert_empty_projlead_errmsg)
        if assert_empty_projlead_errmsg=="Project Lead is required":
            assert True
        time.sleep(1)

    def assert_empty_contact_list_msg(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.cr_proj_contack)).click()
        assert_empty_contact_list_msg=self.driver.find_element(*LocatorsProjectPage.assert_empty_contact_list_msg)
        if assert_empty_contact_list_msg=="List is empty.":
            assert True
        time.sleep(1)

    def assert_proj_cr_success_msg(self):
        self.click_submit_cr_proj()
        assert_proj_cr_success_msg=self.driver.find_element(*LocatorsProjectPage.assert_proj_cr_success_msg)
        if assert_proj_cr_success_msg=="Project data are saved successfully.":
            assert True
        time.sleep(1)

    def assert_proj_del_success_msg(self):
        self.click_submit_cr_proj()
        assert_proj_del_success_msg=self.driver.find_element(*LocatorsProjectPage.assert_proj_del_success_msg)
        if assert_proj_del_success_msg=="Project data removed successfully.":
            assert True
        time.sleep(1)

    def assert_projlead_with_projemp(self):
        proj_lead_text=self.driver.find_element(*LocatorsProjectPage.asser_projectlead_with_projemp_text)
        proj_emp_text=self.driver.find_element(*LocatorsProjectPage.assert_projemp_with_projectlead_text)
        if proj_lead_text==proj_emp_text:
            assert True
        time.sleep(1)

    

#    =========================================> 'Add customer' starts here<====================================================================
    def click_addCustomer(self):
        add_cust=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_addCustomer_x))
        self.driver.execute_script("arguments[0].click();", add_cust)
    
    def sk_customer_company(self):
        cust_company=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_company))
        cust_company.send_keys("lu lu lemon")
    
    def sk_customer_street(self):
        customer_street=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_street))
        customer_street.send_keys("Rue champlains")

    def sk_customer_streetNum(self):
        customer_streetNum=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_streetNum))
        customer_streetNum.send_keys("6/5")

    def sk_customer_zipcode(self):
        customer_zipcode=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_zipcode))
        customer_zipcode.send_keys("249011")

    def sk_customer_city(self):
        customer_city=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_city))
        customer_city.send_keys("Lorient")
    
    def click_country_arrow(self):
        cntry_arrow=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.cust_country))
        # ActionChains(self.driver).move_to_element(cntry_arrow).click().perform()
        self.driver.execute_script("arguments[0].click();", cntry_arrow)

    def sel_france(self):
        # self.click_country_arrow()
        france=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.cust_selFrance))
        # ActionChains(self.driver).move_to_element(france).click().perform()
        self.driver.execute_script("arguments[0].click();", france)

    def click_industry_arrow(self):
        industry=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.cust_sel_industry))
        ActionChains(self.driver).move_to_element(industry).click().perform()
        # self.driver.execute_script("arguments[0].click();", industry)

    def click_all_industry(self):
        all_elements=WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(LocatorsProjectPage.cust_sel_industry_allEle))
        for i in all_elements:
            i.click()
            time.sleep(1)

    def click_respon_arrow(self):
        responsibility=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.cust_dd_rspnsblty))
        self.driver.execute_script("arguments[0].click();", responsibility)

    def sel_akshata(self):
        self.click_respon_arrow()
        akshata=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.cust_respon_akshata))
        self.driver.execute_script("arguments[0].click();", akshata)

    def click_whrFund_arrow(self):
        whrfund=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.cust_dd_arrow_whrFund))
        self.driver.execute_script("arguments[0].click();", whrfund)

    def sel_LinkedIn(self):
        self.click_whrFund_arrow()
        linkedIn=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.cust_sel_linkedIn))
        self.driver.execute_script("arguments[0].click();", linkedIn)

    def sk_customer_website(self):
        customer_website=WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_website_address))
        ActionChains(self.driver).move_to_element(customer_website).perform()
        customer_website.send_keys("www.lululemon.com")
       
    def sk_customer_phnNum(self):
        customer_phnNum=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_officePhone))
        customer_phnNum.send_keys("+91 9876545678")

    def sk_cust_technology(self):
        cust_technology=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_technologies))
        cust_technology.send_keys("xyz")

    def sk_cust_email(self):
        cust_technology=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_sk_email))
        cust_technology.send_keys("abc@gmail.com")

    def sk_cust_detail(self):
        cust_technology=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_txtField_details))
        cust_technology.send_keys("health based company")

    def click_cust_add_btn(self):
        add_btn=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.cust_add_btn))
        self.driver.execute_script("arguments[0].click();", add_btn)

    # =========================================>close of 'Add customer'<====================================================================

    # ============================================>start of 'Add contact'<================================================================
    def click_add_contact_btn(self):
        add_con_btn=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_contact_btn))
        self.driver.execute_script("arguments[0].click();", add_con_btn)

    def click_add_con_login_btn(self):
        add_con_login_btn=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_login_btn))
        self.driver.execute_script("arguments[0].click();", add_con_login_btn)

    def click_add_con_inactive_btn(self):
        add_con_inactive_btn=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_inactive_btn))
        self.driver.execute_script("arguments[0].click();", add_con_inactive_btn)

    def sk_add_con_fname(self):
        add_con_fname=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_fname))
        add_con_fname.send_keys("lakshmi")

    def sk_add_con_lname(self):
        add_con_lname=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_lname))
        add_con_lname.send_keys("s")

    def sk_add_con_jobrole(self):
        add_con_jobrole=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_jobrole))
        add_con_jobrole.send_keys("QA")

    def sk_add_con_telephone(self):
        add_con_telephone=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_telephone))
        add_con_telephone.send_keys("9999999999")

    def sk_add_con_mobile(self):
        add_con_mobile=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_mobile))
        add_con_mobile.send_keys("9999999999")

    def sk_add_con_email(self):
        add_con_email=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_email))
        add_con_email.send_keys("lasya@gmail.com")

    def sk_add_con_DOB(self):
        add_con_DOB=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_DOB))
        add_con_DOB.send_keys("24.06.1990")

    def sk_add_con_interest(self):
        add_con_interest=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_interest))
        add_con_interest.send_keys("24.06.1990")

    def sk_add_con_updates(self):
        add_con_updates=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_updates))
        add_con_updates.send_keys("24.06.1990")

    def click_add_con_btnAdd(self):
        add_con_btnAdd=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.add_con_btnAdd))
        add_con_btnAdd.click()
    
 # ==========================================> End of 'Add contact' <================================================================

# ==========================================> Action button features <================================================================
    def click_3dots(self):
        threedots=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_3dots_xpath))
        ActionChains(self.driver).move_to_element(threedots).click().perform()
        # threedots.click()
        time.sleep(2)

    def click_contents_3dots(self):
        list_data5=[]
        list_eachEle=[]
        self.click_3dots ()
        three_elements=WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(LocatorsProjectPage.contents_3dots_xpath))
        for each_element in three_elements:
            list_eachEle.append(each_element.text)

        for r in range(18,22):
            data5=XLUtils.readData(self.path,"Project_page",r,1)
            list_data5.append(data5)
        print(list_data5)
        print(list_eachEle)

        for i in range(0,len(list_data5)) :
            for s in range(18,22):
                if list_data5[i]==list_eachEle[i]:
                    XLUtils.writeData(self.path,"Project_page",s,4,"pass")
                    XLUtils.fillGreenColor(self.path,"Project_page",s,4)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Project_page",s,4,"failed")
                    XLUtils.fillRedColor(self.path,"Project_page",s,4)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="projects_Fail", attachment_type=AttachmentType.PNG)
                    assert False
                    
    def click_addMilestone(self):
        milestone=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_3dots_milestone))
        milestone.click()
        self.click_3dots()
        milestone=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_3dots_milestone))
        milestone.click()

    def click_3dots_addsprint(self):
        addsprint=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsProjectPage.btn_3dots_addSprint))
        ActionChains(self.driver).move_to_element(addsprint).click().perform()

    def assert_sprintPage_heading(self):
        assert_sprint_H=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsProjectPage.assert_sprint_headline))
        if assert_sprint_H=="Sprint":
            assert True
        time.sleep(1)

    def send_keys_sprintname(self):
        sprintname=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsProjectPage.txtfield_sprintname_x))
        ActionChains(self.driver).move_to_element(sprintname).perform()
        sprintname.send_keys("tiger")

    def assert_BV_sprint_errMsg(self):
        self.btn_add_sprint_3dots()
        assert_sprint_BV_errMsg=self.driver.find_element(*LocatorsProjectPage.assert_BV_sprint_errMsg)
        if assert_sprint_BV_errMsg=="Please enter less than 2 characters":
            assert True
        time.sleep(1)

    def assert_empty_sprint_errMsg(self):
        self.btn_add_sprint_3dots()
        assert_empty_sprint=self.driver.find_element(*LocatorsProjectPage.assert_empty_sprint_errMsg)
        if assert_empty_sprint=="Sprint Name is required":
            assert True
        time.sleep(1)

    def assert_repeatSprint_errMsg(self):
        self.btn_add_sprint_3dots()
        assert_repeatSprint_errMsg=self.driver.find_element(*LocatorsProjectPage.assert_repeatSprint_errMsg)
        if assert_repeatSprint_errMsg==" Sprint name already exists in this project. ":
            assert True
        time.sleep(1)

    def btn_addFooter_sprint_3dots(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_addSprint_add)).click()

    def assert_start_dt_sprint(self):
        assert_sprint_startdate=self.driver.find_element(*LocatorsProjectPage.assert_sprint_startdate)
        if assert_sprint_startdate=="Start Date":
            assert True

    def assert_end_dt_sprint(self):
        assert_sprint_enddate=self.driver.find_element(*LocatorsProjectPage.assert_sprint_enddate)
        if assert_sprint_enddate=="End Date":
            assert True

    def sendkeys_description(self):
        description=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LocatorsProjectPage.txtfield_description_x))
        ActionChains(self.driver).move_to_element(description).perform()
        description.send_keys("first sprint-0.0.1")

    def dd_arrow_sprint(self):
        click_arrow=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.dd_arrow_sprint))
        ActionChains(self.driver).move_to_element(click_arrow).perform()
        click_arrow.click()

    def click_3dots_delete(self):
        delete=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsProjectPage.btn_3dots_delete))
        ActionChains(self.driver).move_to_element(delete).click().perform()
        time.sleep(1)

    def click_3dots_delCancel(self):
        cancel_btn=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_3dots_del_cancel))
        self.driver.execute_script("arguments[0].click();", cancel_btn)
        time.sleep(1)

    def click_3dots_del_del(self):
        del_btn=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsProjectPage.btn_3dots_del_delete))
        self.driver.execute_script("arguments[0].click();", del_btn)
        time.sleep(1)





    # def dd_sprint_4ele(self):
    #     expect=["MS1","DS","ps"]
    #     four_elements=self.driver.find_elements(*LocatorsProjectPage.dd_sprint_4ele_x)
    #     for i in range(len(four_elements)):
    #         each_element.click()
    #         time.sleep(2)
    #         if four_elements[i].text == expect[0]:
           
            


    

    


   

    

    

    


    

    

    