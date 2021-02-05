from pages.RegistationFormPage import RegistationFormPage
from fixtures.TestConstrains import registration_from_data

reg_form_one_data = registration_from_data


def test_registration_form_one(driver):
    form_one = RegistationFormPage(driver)
    form_one.fill_form_one(reg_form_one_data)
