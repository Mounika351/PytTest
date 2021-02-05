from pages.FileupLoadPage import FileUploadPage


def test_file_upload(driver):
    file1 = FileUploadPage(driver)
    file1.uploading_file()
