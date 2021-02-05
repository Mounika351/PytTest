from selenium.webdriver.support.select import By

single_frame = 'frameOne'
frame_place1 = (By.CSS_SELECTOR, '[href="#singleFrame"]')

# first_alert locators
alertone = (By.CSS_SELECTOR, '[href="#alertOne"]')
alertone_click = (By.CSS_SELECTOR, '[onclick="alertone()"]')

# second alert locators
alerttwo = (By.CSS_SELECTOR, '[href="#alertTwo"]')
alerttwo_click = (By.CSS_SELECTOR, '[onclick="alerttwo()"]')

# third alert locators
alertthree = (By.CSS_SELECTOR, '[href="#alertThree"]')
alertthree_click = (By.CSS_SELECTOR, '[onclick="alertthree()"]')

