from selenium import webdriver
from page import GoogleTranslate


GOOGLE_TRANSLATE_URL = "https://translate.google.com/"

example_phrase = "youngblood, say you want me back in your life"
example_language = 'spanish'

driver = webdriver.Chrome()
driver.get(GOOGLE_TRANSLATE_URL)

translator = GoogleTranslate(driver)

translator.select_language(example_language)
translator.type_phrase(example_phrase)
translator.copy_translation()
# TODO write to the file


translator.clear_phrase()


# when finished
driver.quit()
