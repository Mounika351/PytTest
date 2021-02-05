from pages.locators import CommonLocators, IframeSingleLocators
from utilities.CommonHelper import CommonHelper
from fixtures import TestConstrains


class IframeSingle:

    def __init__(self, driver):
        self.driver = driver
        self.common_helper = CommonHelper(driver)

    def switch_to_frame(self):
        self.driver.switch_to.frame(IframeSingleLocators.single_frame)

    def frame_place(self):
        self.common_helper.goto_pages('Switch To', 'Frames')
        self.driver.find_element(*IframeSingleLocators.frame_place1).click()
        self.switch_to_frame()

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def first_alert(self):
        self.frame_place()
        self.driver.find_element(*IframeSingleLocators.alertone).click()
        self.driver.find_element(*IframeSingleLocators.alertone_click).click()
        self.alert_accept()

    def second_alert(self):
        self.driver.find_element(*IframeSingleLocators.alerttwo).click()
        self.driver.find_element(*IframeSingleLocators.alerttwo_click).click()
        self.alert_accept()

    def third_alert(self):
        self.driver.find_element(*IframeSingleLocators.alertthree).click()
        self.driver.find_element(*IframeSingleLocators.alertthree_click).click()
        self.driver.switch_to.alert.send_keys(TestConstrains.name)
        self.alert_accept()
        self.driver.switch_to.default_content()
