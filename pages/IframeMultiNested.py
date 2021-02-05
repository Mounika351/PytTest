from selenium.webdriver.common.by import By
from utilities.CommonHelper import CommonHelper
from pages.locators import CommonLocators
from pages.locators import IframeMultiNestedLocators
from fixtures import TestConstrains

class IframeMultiNested:

    def __init__(self, driver):
        self.driver = driver
        self.common_helper = CommonHelper(driver)

    def switch_default(self):
        self.driver.switch_to.default_content()

    def switch_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def details(self):
        name = self.driver.find_element(*IframeMultiNestedLocators.trainer_name).text
        address = self.driver.find_element(*IframeMultiNestedLocators.trainer_address).text
        assert name == CommonLocators.trainerName
        assert address == CommonLocators.trainerAddress

    def multi_frame1(self):
        self.common_helper.goto_pages('Others', 'Multiple Frame')
        self.driver.find_element(*IframeMultiNestedLocators.message_field).send_keys(TestConstrains.message)
        self.driver.find_element(*CommonLocators.submitBtn).click()
        self.switch_frame('frame-urbanpro')
        self.details()
        self.switch_default()

    def nested_frame1(self):
        self.driver.get(CommonLocators.link)
        self.common_helper.goto_pages('Others', 'Nested Frame')
        self.switch_frame(0)
        self.driver.find_element(*IframeMultiNestedLocators.message_field).send_keys(TestConstrains.message)
        self.driver.find_element(*CommonLocators.submitBtn).click()
        self.switch_default()
        self.switch_frame('frame-dummy')
        self.details()
        self.switch_default()
