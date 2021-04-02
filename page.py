from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from locators import GoogleTranslateLocators


class GoogleTranslate(object):
    """ Google Translate webpage """

    def __init__(self, driver):
        self.driver = driver

    def select_language(self, language):
        """ select a language """
        # TODO

    def type_phrase(self, phrase):
        """ Type an english phrase into google translate """
        # TODO

    def copy_translation(self):
        """ Hit the copy button for the translation """
        # TODO

    def clear_phrase(self):
        """ Clear the phrase you typed in for translation """
        # TODO
