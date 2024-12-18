from utilities import XLUtils
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.locators import LocatorsDashboardPage
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure


class DashboardPage():

    path=r"C:\Nagalakshmi\PythonPractice\BPMT admin_login\testdata\pythonSelDemo.xlsx"

    def __init__(self,driver):
        self.driver=driver

    def German_lang_assert(self):
        langAssert=XLUtils.readData(self.path,"DB_page_adminlogin",23,1)
        print(langAssert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsDashboardPage.German_assertion_x))
        print((self.driver.find_element(*LocatorsDashboardPage.German_assertion_x)).text)
        if (self.driver.find_element(*LocatorsDashboardPage.German_assertion_x)).text == langAssert:
            XLUtils.writeData(self.path,"DB_page_adminlogin",23,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",23,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",23,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",23,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            
        
    def click_language(self):
        prof_pic=WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(LocatorsDashboardPage.ddbtn_lang_xpath))
        # prof_pic=self.driver.find_element(*LocatorsDashboardPage.ddbtn_lang_xpath)
        self.driver.execute_script("arguments[0].click();", prof_pic)
        
    def click_english(self):
        prof_pic=self.driver.find_element(*LocatorsDashboardPage.dd_engLang_xpath)
        self.driver.execute_script("arguments[0].click();", prof_pic)
        time.sleep(2)

    def click_project_leftside(self):
        time.sleep(1)
        link_project=self.driver.find_element(*LocatorsDashboardPage.link_project_xpath)
        self.driver.execute_script("arguments[0].click();", link_project)

    def click_notification_icon(self):
        ntfn_btn=self.driver.find_element(*LocatorsDashboardPage.notification_img_x)
        ActionChains(self.driver).move_to_element(ntfn_btn).click().perform()
         #we given locator of notification button click in another method(def ntfn_text_assert(self):), so no need of this method

    def ntfn_text_assert(self):
        assert_ntfnTxt=XLUtils.readData(self.path,"DB_page_adminlogin",24,1)
        print(assert_ntfnTxt)
        # ntfn_btn=self.driver.find_element(*LocatorsDashboardPage.notification_img_x)
        # self.driver.execute_script("arguments[0].click();", ntfn_btn)
        webElement=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LocatorsDashboardPage.label_ntfnAssert_x)).text
        print(webElement)
        if webElement == assert_ntfnTxt:
            XLUtils.writeData(self.path,"DB_page_adminlogin",24,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",24,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",24,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",24,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False 
        
    def markAsRead_text_assert(self):
        assert_markAsTxt=XLUtils.readData(self.path,"DB_page_adminlogin",25,1)
        print(assert_markAsTxt)
        webElement=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LocatorsDashboardPage.label_markasread_assert)).text
        print(webElement)
        if (self.driver.find_element(*LocatorsDashboardPage.label_markasread_assert)).text == assert_markAsTxt:
            XLUtils.writeData(self.path,"DB_page_adminlogin",25,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",25,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",25,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",25,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        
    def viewAllNtfn_text_assert(self):
        assert_viewAllntfnTxt=XLUtils.readData(self.path,"DB_page_adminlogin",26,1)
        print(assert_viewAllntfnTxt)
        webElement=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LocatorsDashboardPage.label_viewAllNtfn_assert)).text
        print(webElement)
        # assert_viewAllntfnTxt=self.driver.find_element(*LocatorsDashboardPage.label_viewAllNtfn_assert)
        # self.driver.execute_script("arguments[0].click();", assert_viewAllntfnTxt)
        if webElement == assert_viewAllntfnTxt:
            XLUtils.writeData(self.path,"DB_page_adminlogin",26,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",26,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",26,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",26,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(1)
    
    def scroll_NtfnPage(self):
        try:
            ActionChains(self.driver).move_to_element(self.driver.find_element(*LocatorsDashboardPage.scroll_ntfnScreen_x)).perform()
        except:
            pass
        time.sleep(2)

    def menu_icon(self):
        for i in range(0,2):
            if i<5:
                menu=self.driver.find_element(*LocatorsDashboardPage.img_menuIcon_x)
                self.driver.execute_script("arguments[0].click();", menu)
                time.sleep(2)
        

    def click_dashboard_pagelink(self):
        dbpage=self.driver.find_element(*LocatorsDashboardPage.link_dashboard_x)
        self.driver.execute_script("arguments[0].click();", dbpage)
        time.sleep(2)

    def Kanban_H1(self):
        data1=XLUtils.readData(self.path,"DB_page_adminlogin",2,1) #to fetch 'kanban' for assertion with locator
        print(data1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsDashboardPage.label_H_Kanban_x))
       
        if (self.driver.find_element(*LocatorsDashboardPage.label_H_Kanban_x)).text == data1:
            XLUtils.writeData(self.path,"DB_page_adminlogin",2,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",2,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",2,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",2,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False 

    def Kanban_subFeatures(self):
        data2_list=[]
        list_eachEle=[]
       
        four_elements=self.driver.find_elements(*LocatorsDashboardPage.kanban_subFeature_x)
        for each_element in four_elements[0:]:
            list_eachEle.append(each_element.text)

        for r in range(3,7):
            data2=XLUtils.readData(self.path,"DB_page_adminlogin",r,1)
            data2_list.append(data2)
            
        for i in range(0,len(data2_list)) :
            for s in range(3,7):
                if data2_list[i]==list_eachEle[i]:
                    XLUtils.writeData(self.path,"DB_page_adminlogin",s,4,"pass")
                    XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",s,4)
                    assert True
                else:
                    XLUtils.writeData(self.path,"DB_page_adminlogin",s,4,"failed")
                    XLUtils.fillRedColor(self.path,"DB_page_adminlogin",s,4)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False 

    def kanban_fullview_btn(self):
        data3=XLUtils.readData(self.path,"DB_page_adminlogin",7,1) #to fetch 'fullview' for assertion with locator
        print(data3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsDashboardPage.label_fullview_x))
    
        if (self.driver.find_element(*LocatorsDashboardPage.label_fullview_x)).text == data3:
            XLUtils.writeData(self.path,"DB_page_adminlogin",7,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",7,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",7,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",7,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_kanban_fullview(self):
        fullview=self.driver.find_element(*LocatorsDashboardPage.img_fullview_x)
        self.driver.execute_script("arguments[0].click();", fullview)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsDashboardPage.img_fullview_x)).click()

    def click_dd_analyse(self):
        link1=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsDashboardPage.dd_kanbanAnalyse_x))
        # link1=self.driver.find_element(*LocatorsDashboardPage.dd_kanbanAnalyse_x)
        ActionChains(self.driver).move_to_element(link1).click().perform()
        # self.driver.execute_script("arguments[0].click();", link1)
        

    def click_dd_close(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsDashboardPage.btn_kanbanAnalyze_close)).click()

    def click_cancel_kanAna_dd(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsDashboardPage.btn_cancel_diaB_kanAna_x)).click()
    
    def department_H2(self):
        data4=XLUtils.readData(self.path,"DB_page_adminlogin",8,1) #to fetch 'fullview' for assertion with locator
        print(data4)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsDashboardPage.label_deptOverview_x))
    
        if (self.driver.find_element(*LocatorsDashboardPage.label_deptOverview_x)).text == data4:
            XLUtils.writeData(self.path,"DB_page_adminlogin",8,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",8,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",8,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",8,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_ddArrow_date(self):
        dateArrow=self.driver.find_element(*LocatorsDashboardPage.dd_datearrow_x)
        self.driver.execute_script("arguments[0].click();", dateArrow)
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocatorsDashboardPage.dd_datearrow_x)).click()
       
    def department_date(self):
        list_data5=[]
        list_eachEle=[]
        self.click_ddArrow_date ()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(LocatorsDashboardPage.dd_3elements))
        three_elements=self.driver.find_elements(*LocatorsDashboardPage.dd_3elements)
        for each_element in three_elements[0:]:
            list_eachEle.append(each_element.text)

        for r in range(9,12):
            data5=XLUtils.readData(self.path,"DB_page_adminlogin",r,1)
            list_data5.append(data5)
        print(list_data5)
        print(list_eachEle)

        for i in range(0,len(list_data5)) :
            for s in range(9,12):
                if list_data5[i]==list_eachEle[i]:
                    XLUtils.writeData(self.path,"DB_page_adminlogin",s,4,"pass")
                    XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",s,4)
                    assert True
                else:
                    XLUtils.writeData(self.path,"DB_page_adminlogin",s,4,"failed")
                    XLUtils.fillRedColor(self.path,"DB_page_adminlogin",s,4)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False
        time.sleep(1) 

    def click_department_date(self):
        dateArrow=self.driver.find_element(*LocatorsDashboardPage.dd_datearrow_x)
        self.driver.execute_script("arguments[0].click();", dateArrow)
       
        three_elements= WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(LocatorsDashboardPage.dd_3elements))
        print(three_elements)
        for element in range(len(three_elements)):

            dateArrow=self.driver.find_element(*LocatorsDashboardPage.dd_datearrow_x)
            self.driver.execute_script("arguments[0].click();", dateArrow)
    
            names_of_elements=self.driver.find_elements(*LocatorsDashboardPage.dd_3elements)
            assert_text_beforeClick=names_of_elements[element].text
            print(assert_text_beforeClick)

            names_of_elements[element].click()
            assert_text_afterClick=names_of_elements[element].text
            print(assert_text_afterClick)

            assert assert_text_beforeClick==assert_text_afterClick    

            
    def department_subFeatures(self):
        list_data6=[]
        list_eachEle=[]
       
        three_elements=self.driver.find_elements(*LocatorsDashboardPage.Actual_meet_RD)
        for each_element in three_elements[0:]:
            list_eachEle.append(each_element.text)

        for r in range(12,15):
            data6=XLUtils.readData(self.path,"DB_page_adminlogin",r,1)
            list_data6.append(data6)
        print(list_data6)
        print(list_eachEle)
            
        for i in range(0,len(list_data6)) :
            for s in range(12,15):
                if list_data6[i]==list_eachEle[i]:
                    XLUtils.writeData(self.path,"DB_page_adminlogin",s,4,"pass")
                    XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",s,4)
                    assert True
                else:
                    XLUtils.writeData(self.path,"DB_page_adminlogin",s,4,"failed")
                    XLUtils.fillRedColor(self.path,"DB_page_adminlogin",s,4)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False 

    def click_Dept_overview_subfeature(self):
        three_buttons= WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(LocatorsDashboardPage.three_buttons_Dept4Ele))
        print("Above loop", len(three_buttons))
        print("Above loop", type(three_buttons))
        for i in range(1,len(three_buttons)):
            print(i)
            each_button=self.driver.find_elements(*LocatorsDashboardPage.three_buttons_Dept4Ele)
            print("inside loop", len(each_button))
            print("inside loop", type(each_button))
            ActionChains(self.driver).move_to_element(each_button[i]).click().perform()
            

    def click_month(self):
            self.click_ddArrow_date ()
            month=self.driver.find_element(*LocatorsDashboardPage.label_deptMonth_x)
            self.driver.execute_script("arguments[0].click();", month)
            assert_input1=self.driver.find_elements(By.XPATH, "//input[@id='md-input-vysesg528'][@class='md-input md-input md-select-value']")
            if assert_input1=="Month":
                assert True
            time.sleep(1)
        
    def click_week(self):
        self.click_ddArrow_date ()
        week=self.driver.find_element(*LocatorsDashboardPage.label_deptWeek_x)
        self.driver.execute_script("arguments[0].click();", week)
        assert_input2=self.driver.find_elements(By.XPATH, "//input[@id='md-input-vysesg528'][@class='md-input md-input md-select-value']")
        if assert_input2=="Week":
            assert True
        time.sleep(1)

    def click_day(self):
        self.click_ddArrow_date ()
        day=self.driver.find_element(*LocatorsDashboardPage.label_deptDay_x)
        self.driver.execute_script("arguments[0].click();", day)
        assert_input3=self.driver.find_elements(By.XPATH, "//input[@id='md-input-vysesg528'][@class='md-input md-input md-select-value']")
        if assert_input3=="Day":
            assert True
        time.sleep(1)


    def click_actualLink_dept(self):
        link1=self.driver.find_element(*LocatorsDashboardPage.label_deptActual_x)
        ActionChains(self.driver).move_to_element(link1).click().perform()
        # self.driver.execute_script("arguments[0].click();", link1)
        time.sleep(1)
        
    def click_meetingsLink_dept(self):
        link2=self.driver.find_element(*LocatorsDashboardPage.label_deptmeetings_x)
        self.driver.execute_script("arguments[0].click();", link2)
        time.sleep(1)
         # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsDashboardPage.label_deptmeetings_x)).click()

    def click_RDlink_dept(self):
        link3=self.driver.find_element(*LocatorsDashboardPage.label_RD_x)
        self.driver.execute_script("arguments[0].click();", link3)
        
    def calender_H1(self):
        data7=XLUtils.readData(self.path,"DB_page_adminlogin",15,1) 
        print(data7)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsDashboardPage.label_H_Calender_x))
       
        if (self.driver.find_element(*LocatorsDashboardPage.label_H_Calender_x)).text == data7:
            XLUtils.writeData(self.path,"DB_page_adminlogin",15,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",15,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",15,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",15,4)
            assert False 


    def calender_sub_features(self):
        list_data8=[]
        list_eachEle=[]
       
        seven_elements=self.driver.find_elements(*LocatorsDashboardPage.all_labels_of_calender_x)
        for each_element in seven_elements[0:]:
            list_eachEle.append(each_element.text)

        for r in range(16,23):
            data6=XLUtils.readData(self.path,"DB_page_adminlogin",r,1)
            list_data8.append(data6)
        print(list_data8)
        print(list_eachEle)
            
        for i in range(0,len(list_data8)) :
            for s in range(16,23):
                if list_data8[i]==list_eachEle[i]:
                    XLUtils.writeData(self.path,"DB_page_adminlogin",s,4,"pass")
                    XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",s,4)
                    assert True
                else:
                    XLUtils.writeData(self.path,"DB_page_adminlogin",s,4,"failed")
                    XLUtils.fillRedColor(self.path,"DB_page_adminlogin",s,4)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False  

    def click_calender_fullview(self):
        fullview2=self.driver.find_element(*LocatorsDashboardPage.img_Calfullview_x)
        self.driver.execute_script("arguments[0].click();", fullview2)
        time.sleep(1)
     
    def click_cal_reverseArrow(self):
        arrow1=self.driver.find_element(*LocatorsDashboardPage.img_reverseArrow_x)
        self.driver.execute_script("arguments[0].click();", arrow1)
        time.sleep(1)
        
    def click_cal_forwardArrow(self):
        arrow2=self.driver.find_element(*LocatorsDashboardPage.img_forwardArrow_x)
        self.driver.execute_script("arguments[0].click();", arrow2)
        time.sleep(1)

    def scrollPage(self):
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        # ActionChains(self.driver).send_keys(Keys.SPACE).perform()    
        # ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    def scroll_down(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='horizontal-of pb-20'] div:nth-child(2) div:nth-child(2) div:nth-child(2) p:nth-child(1)")))
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def scroll_right(self):
        scrollBar = self.driver.find_element(*LocatorsDashboardPage.right_scrolling)
        webdriver.ActionChains(self.driver).move_to_element(scrollBar).click_and_hold(scrollBar).move_by_offset(0,30).release().perform()
        # ActionChains(self.driver).move_to_element(scrollBar).perform()
        # time.sleep(1)

    def calender_hor_scrollbar(self):
        cal_scroll=self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[8]/div[2]/div[1]/img[2]")
        webdriver.ActionChains(self.driver).move_to_element(cal_scroll).click_and_hold(cal_scroll).move_by_offset(0,30).release().perform()

    def version_text(self):
        footer_version=XLUtils.readData(self.path,"DB_page_adminlogin",27,1)
        print(footer_version)
        webElement=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsDashboardPage.txt_footer_version)).text
        print(webElement)
        if (self.driver.find_element(*LocatorsDashboardPage.txt_footer_version)).text == footer_version:
            XLUtils.writeData(self.path,"DB_page_adminlogin",27,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",27,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",27,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",27,4)
            assert False 

    def company_Nametext(self):
        footer_nameCompany=XLUtils.readData(self.path,"DB_page_adminlogin",28,1)
        print(footer_nameCompany)
        webElement=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsDashboardPage.txt_footer_co_name)).text
        print(webElement)
        if (self.driver.find_element(*LocatorsDashboardPage.txt_footer_co_name)).text == footer_nameCompany:
            XLUtils.writeData(self.path,"DB_page_adminlogin",28,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page_adminlogin",28,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page_adminlogin",28,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page_adminlogin",28,4)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False 

    def drag_drop1(self):
        ActionChains(self.driver)
        # source=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsDashboardPage.dnd_qualify_kanban_drag))
        # target= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsDashboardPage.dnd_analyze_drop))
        source=self.driver.find_element(*LocatorsDashboardPage.dnd_qualify_kanban_drag)
        target=self.driver.find_element(*LocatorsDashboardPage.dnd_analyze_drop)
      
        # action1.drag_and_drop(source, target).perform()
        # action1.click_and_hold(source).pause(2).move_to_element(target).perform()
        # action1.click_and_hold(on_element=source).move_to_element(target).perform()
        webdriver.ActionChains(self.driver).click_and_hold(on_element=source).drag_and_drop(source, target).release().perform()
        
        # XLUtils.load_excel(self.path,"DB_page")
        # data = XLUtils.get_data_as_list_tuples()
        # print(data)
        # for item in data:
        #     print(item[2])    #To print only 3rd col of data

        # self.rows=XLUtils.getRowCount(self.path, "DB_page") #to fetch entire first column data 
        # for r in range(2, self.rows):
        #     entire_colData= XLUtils.readData(self.path,"DB_page",r,1)
        #     print(entire_colData) 

        # def click_month(self):
        #     self.click_ddArrow_date ()
        #     month=self.driver.find_element(*LocatorsDashboardPage.label_deptMonth_x)
        #     self.driver.execute_script("arguments[0].click();", month)
        #     assert_input1=self.driver.find_elements(By.XPATH, "//input[@id='md-input-vysesg528'][@class='md-input md-input md-select-value']")
        #     if assert_input1=="Month":
        #         assert True
        #     time.sleep(1)
        
        # def click_week(self):
        #     self.click_ddArrow_date ()
        #     week=self.driver.find_element(*LocatorsDashboardPage.label_deptWeek_x)
        #     self.driver.execute_script("arguments[0].click();", week)
        #     assert_input2=self.driver.find_elements(By.XPATH, "//input[@id='md-input-vysesg528'][@class='md-input md-input md-select-value']")
        #     if assert_input2=="Week":
        #         assert True
        #     time.sleep(1)

        # def click_day(self):
        #     self.click_ddArrow_date ()
        #     day=self.driver.find_element(*LocatorsDashboardPage.label_deptDay_x)
        #     self.driver.execute_script("arguments[0].click();", day)
        #     assert_input3=self.driver.find_elements(By.XPATH, "//input[@id='md-input-vysesg528'][@class='md-input md-input md-select-value']")
        #     if assert_input3=="Day":
        #         assert True
        #     time.sleep(1)



   
    
    

    

