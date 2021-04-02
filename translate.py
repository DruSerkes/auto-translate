from selenium import webdriver
from page import GoogleTranslate
from languages import LANGUAGES
from time import sleep

GOOGLE_TRANSLATE_URL = "https://translate.google.com/"

# example_phrase = "youngblood, say you want me back in your life"
# example_language = 'spanish'

phrases_to_translate = []

with open('phrases.txt', 'r') as f:
    for phrase in f:
        phrases_to_translate.append(phrase.rstrip())


print(f'Phrases to translate: {phrases_to_translate}')

# driver = webdriver.Chrome()
# driver.get(GOOGLE_TRANSLATE_URL)
# translator = GoogleTranslate(driver)

# def get_translated_phrase(translator, language, last_translation):
#     translator.select_language(language)
#     translation = translator.read_translated_phrase()
#     return translation


def add_translation_to_file(language, translation):
    with open(f'translations-{language}', 'a') as f:
        f.write(translation + '\n')


def translate_phrases(phrases, language):
    """ 
    Translate a list of phrases into a language
    phrases: List 
    language: string
    output: writes translations to a file in this directory  
    """
    # driver = webdriver.Chrome()
    # driver.get(GOOGLE_TRANSLATE_URL)
    # translator = GoogleTranslate(driver)

    translator.select_language(language)
    for phrase in phrases:
        translator.type_phrase_to_translate(phrase)
        sleep(1)
        translated_phrase = translator.read_translated_phrase()
        add_translation_to_file(language, translated_phrase)
    # driver.quit()


def translate_phrases_into_languages(phrases=phrases_to_translate, languages=LANGUAGES):
    for language in LANGUAGES:
        translate_phrases(phrases_to_translate, language)


def auto_translate(phrases=phrases_to_translate, languages=LANGUAGES):
    """ 
    Automatically translates each phrase into each language via chrome & google translate 
    This runs O(n^2), so it may take some time depending on how many phrases and languages you input
    """
    driver = webdriver.Chrome()
    driver.get(GOOGLE_TRANSLATE_URL)
    translator = GoogleTranslate(driver)
    translate_phrases_into_languages(phrases, languages)

    driver.quit()
    print('PROCESS COMPLETE!')
