from selenium.webdriver.common.by import By


class GoogleTranslateLocators(object):
    """ Locators for Google Translate """
    RIGHT_DROPDOWN_BUTTON = (
        By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[5]/button')
    LEFT_TEXTAREA = (
        By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
    TRANSLATED_TEXT = (
        By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')
    LEFT_CLEAR_BUTTON = (By.XPATH, '//*[@id="ow41"]/div/span/button')
    LANGUAGE_SEARCH_INPUT = (
        By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[2]/div/div[2]/input')
    LANGUAGE = (
        By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[2]/div/div[4]/div/div/div[2]/span')
    LANGUAGE_LIST = (
        By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[2]/div/div[3]/div')
    TEXT_TRANSLATING = (
        By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[2]')
    LEFT_X_BUTTON = (By.XPATH, '//*[@id="ow41"]/div[1]/span/button')
