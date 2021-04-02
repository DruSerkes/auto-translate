from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import GoogleTranslateLocators
from elements import LeftInputElement, LanguageSearchInputElement

GOOGLE_TRANSLATE_URL = "https://translate.google.com/"


class GoogleTranslate(object):
    """ Google Translate webpage """
    translation_text = LeftInputElement()
    language_search = LanguageSearchInputElement()

    def __init__(self, driver):
        self.driver = driver
        self.delay = 5
        self.driver.get(GOOGLE_TRANSLATE_URL)

    def select_language(self, language):
        """ select a language """
        language_options_button = self.driver.find_element(
            *GoogleTranslateLocators.RIGHT_DROPDOWN_BUTTON)
        language_options_button.click()

        WebDriverWait(self.driver, self.delay).until(
            lambda driver: driver.find_element(*GoogleTranslateLocators.LANGUAGE_LIST))

        self.language_search = language

        language_button = WebDriverWait(self.driver, self.delay).until(
            lambda driver: driver.find_element(*GoogleTranslateLocators.LANGUAGE))
        language_button.click()

    def type_phrase(self, phrase):
        """ Type an english phrase into google translate """
        self.translation_text = phrase

    # def copy_translation(self):
    #     """ Hit the copy button for the translation """
    #     # TODO

    # def clear_phrase(self):
    #     """ Clear the phrase you typed in for translation """
    #     # TODO


# WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
       #     *GoogleTranslateLocators.RIGHT_DROPDOWN_BUTTON))
