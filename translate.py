from selenium import webdriver
from page import GoogleTranslate
from languages import LANGUAGES
from time import sleep

GOOGLE_TRANSLATE_URL = "https://translate.google.com/"
TRANSLATIONS_DIRECTORY = './translations'

# example_phrase = "youngblood, say you want me back in your life"
# example_language = 'spanish'

phrases_to_translate = []

with open('phrases.txt', 'r') as f:
    for phrase in f:
        phrases_to_translate.append(phrase.rstrip())

print(f'Phrases to translate: {phrases_to_translate}')


def add_translation_to_file(language, translation):
    """ Write translation to a file in the translations/ directory  """
    with open(f'{TRANSLATIONS_DIRECTORY}/{language}', 'a') as f:
        f.write(translation + '\n')


def translate_phrases(translator, phrases, language):
    """ Translate a list of phrases into a language """
    for phrase in phrases:
        translator.type_phrase_to_translate(phrase)
        sleep(0.5)
        translated_phrase = translator.read_translated_phrase()
        add_translation_to_file(language, translated_phrase)


def translate_phrases_into_languages(translator, phrases, languages):
    """ Translate a list of phrases into a list of languages """
    for language in LANGUAGES:
        translator.open_new_tab(GOOGLE_TRANSLATE_URL)
        translator.select_language(language)
        translate_phrases(translator, phrases_to_translate, language)
        translator.close_current_tab()


def auto_translate(phrases=phrases_to_translate, languages=LANGUAGES):
    """ 
    Automatically translates each phrase into each language via chrome & google translate \n
    This runs O(n^2), so it may take some time
    """
    driver = webdriver.Chrome()
    translator = GoogleTranslate(driver)
    translate_phrases_into_languages(translator, phrases, languages)

    driver.quit()


if __name__ == '__main__':
    auto_translate()
    print('PROCESS COMPLETE!')
