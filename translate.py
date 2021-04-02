from selenium import webdriver
from page import GoogleTranslate
from time import sleep


example_phrase = "youngblood, say you want me back in your life"
example_language = 'spanish'

driver = webdriver.Chrome()

translator = GoogleTranslate(driver)

translator.select_language(example_language)
translator.type_phrase(example_phrase)
# translator.copy_translation()
# sleep(3)
# TODO write to the file


# translator.clear_phrase()


# when finished
driver.quit()
