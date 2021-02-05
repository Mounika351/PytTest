from pages.locators import TypingCarosuelLocators,CommonLocators
from utilities.CommonHelper import *


class TypingCarousel:

    def __init__(self, driver):
        self.driver = driver
        self.common_helper = CommonHelper(driver)

    def word_taking(self):
        self.driver.get(CommonLocators.link)
        self.common_helper.goto_pages('Gadgets', 'Typing Carousel')
        word_one = self.driver.find_element(*TypingCarosuelLocators.word).text
        print(word_one)

    def word_taking2(self):
        word_two = self.driver.find_element(*TypingCarosuelLocators.word2).text
        print(word_two)
