from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import GoogleTranslateLocators
from elements import LeftInputElement, LanguageSearchInputElement
from selenium.common.exceptions import ElementNotInteractableException

GOOGLE_TRANSLATE_URL = "https://translate.google.com/"


class GoogleTranslate(object):
    """ Google Translate webpage """
    translation_text = LeftInputElement()
    language_search = LanguageSearchInputElement()

    def __init__(self, driver):
        self.driver = driver
        self.delay = 10
        # self.driver.get(GOOGLE_TRANSLATE_URL)

    def select_language(self, language):
        """ select a language """
        language_options_button = self.driver.find_element(
            *GoogleTranslateLocators.RIGHT_DROPDOWN_BUTTON)
        language_options_button.click()

        WebDriverWait(self.driver, self.delay).until(
            lambda driver: driver.find_element(*GoogleTranslateLocators.LANGUAGE_LIST))
        try:
            self.language_search = language
            language_button = WebDriverWait(self.driver, self.delay).until(
                lambda driver: driver.find_element(*GoogleTranslateLocators.LANGUAGE))
            language_button.click()
        except ElementNotInteractableException:
            self.driver.implicitly_wait(3)
            self.language_search = language
            language_button = WebDriverWait(self.driver, self.delay).until(
                lambda driver: driver.find_element(*GoogleTranslateLocators.LANGUAGE))
            language_button.click()

    def type_phrase_to_translate(self, phrase):
        """ Type an english phrase into google translate """
        try:
            self.translation_text = phrase
        except ElementNotInteractableException:
            self.driver.implicitly_wait(3)
            self.translation_text = phrase

    def read_translated_phrase(self):
        """ Return the translated text """
        # WAIT FOR "TRANSLATING TO BE GONE"
        # text_translating = WebDriverWait(self.driver, self.delay).until(lambda driver: )
        text_translating = self.driver.find_element(
            *GoogleTranslateLocators.TEXT_TRANSLATING)
        WebDriverWait(self.driver, self.delay).until_not(
            EC.visibility_of(text_translating))

        # GET THE TRANSLATED TEXT AND RETURN IT
        translated_text_element = WebDriverWait(self.driver, self.delay).until(
            lambda driver: driver.find_element(*GoogleTranslateLocators.TRANSLATED_TEXT))
        return translated_text_element.text

    def clear_phrase(self):
        """ Clear the phrase you typed in for translation """
        # translation_text = ''
        # FIND THE CLEAR BUTTON
        clear_button = WebDriverWait(self.driver, self.delay).until(
            lambda driver: driver.find_element(*GoogleTranslateLocators.LEFT_X_BUTTON))
        # WAIT FOR IT TO BE CLICKABLE AND CLICK IT
        WebDriverWait(self.driver, self.delay).until(
            EC.element_to_be_clickable(GoogleTranslateLocators.LEFT_X_BUTTON[1]))
        clear_button.click()
