from selenium.webdriver.support import expected_conditions as EC
from pageobjects.locators import LocatorsKanbanPage
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class KanbanPage():

    def __init__(self,driver):
        self.driver=driver

    def drag_drop1(self):
        action1=ActionChains(self.driver)
        # source=self.driver.find_element(*LocatorsKanbanPage().dnd_qualify_kanban_drag)
        # source=self.driver.find_element(*LocatorsKanbanPage().dnd_qualify_kanban_drag)
        # self.driver.execute_script("arguments[0].click();", source)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsKanbanPage.dnd_qualify_kanban_drag))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsKanbanPage.dnd_analyze_drop))
        target=self.driver.find_element(*LocatorsKanbanPage.dnd_analyze_drop)
        source=self.driver.find_element(*LocatorsKanbanPage.dnd_qualify_kanban_drag)
        # action1.move_to_element(source).click().drag_and_drop(source, target).perform()
        # action1.drag_and_drop(source, target).perform()
        # action1.click_and_hold(source).move_to_element(target).perform()
        action1.move_to_element(source).click_and_hold().move_to_element(target).release().perform()
    #     print("moved")
    #     time.sleep(3)

    # def drag_drop2(self):
    #     action2=ActionChains(self.driver)
    #     source=self.driver.find_element(*LocatorsKanbanPage.dnd_qualify_kanban_drag)
    #     self.driver.execute_script("arguments[0].click();", source)
    #     target=self.driver.find_element(*LocatorsKanbanPage.dnd_offer_drop)
    #     action2.drag_and_drop(source, target)
    #     print("moved")
    #     time.sleep(3)

    # def drag_drop3(self):
    #     action3=ActionChains(self.driver)
    #     source=self.driver.find_element(*LocatorsKanbanPage.dnd_qualify_kanban_drag)
    #     self.driver.execute_script("arguments[0].click();", source)
    #     target=self.driver.find_element(*LocatorsKanbanPage.dnd_negotiate_drop)
    #     action3.drag_and_drop(source, target)

    