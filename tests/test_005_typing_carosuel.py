from pages.TypingCarosuel import *


def test_typing_carosuel(driver):
    typing1 = TypingCarousel(driver)
    typing1.word_taking()
    typing1.word_taking2()