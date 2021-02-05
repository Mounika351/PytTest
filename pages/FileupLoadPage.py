from utilities.CommonHelper import CommonHelper
from fixtures import TestConstrains
from pages.locators import FileUploadLocators


class FileUploadPage:

    def __init__(self, driver):
        self.driver = driver
        self.common_helper = CommonHelper(driver)

    def uploading_file(self):
        self.common_helper.goto_pages("Gadgets", "File Upload")
        self.driver.find_element(*FileUploadLocators.image_upload).send_keys(TestConstrains.image_address)
