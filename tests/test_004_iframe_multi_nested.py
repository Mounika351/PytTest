from pages.IframeMultiNested import *


def test_multi_nested_frame(driver):
    multi = IframeMultiNested(driver)
    nested = IframeMultiNested(driver)
    multi.multi_frame1()
    nested.nested_frame1()





