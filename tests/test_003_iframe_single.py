from pages.IframeSingle import *


def test_single_iframe(driver):
    frame1 = IframeSingle(driver)
    frame1.first_alert()
    frame1.second_alert()
    frame1.third_alert()
