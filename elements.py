from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import GoogleTranslateLocators


class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        element = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(*self.locator))
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(self.locator))
        return element.get_attribute("value")


class LeftInputElement(BasePageElement):
    """ the left input for google translate """
    locator = GoogleTranslateLocators.LEFT_TEXTAREA


class LanguageSearchInputElement(BasePageElement):
    """ the language input for google translate """
    locator = GoogleTranslateLocators.LANGUAGE_SEARCH_INPUT
