from selenium.webdriver.common.by import By


class LoginPage():
    
    txt_email_xpath="//input[@type='text']"
    txt_password_xpath="//input[@type='password']"
    btn_login1_xpath="//button[@type='submit']"
    text_Dashboard="//h2[.=' Dashboard ']"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPW(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login1_xpath).click()

    def isTextExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_Dashboard).is_displayed()
        except:
             return False

    