from selenium import webdriver
from page import GoogleTranslate
from languages import LANGUAGES

GOOGLE_TRANSLATE_URL = "https://translate.google.com/"

# example_phrase = "youngblood, say you want me back in your life"
# example_language = 'spanish'

phrases_to_translate = []

with open('phrases.txt', 'r') as f:
    for phrase in f:
        print('phrase: ', phrase.rstrip())
        phrases_to_translate.append(phrase.rstrip())


print(f'Phrases to translate: {phrases_to_translate}')

# driver = webdriver.Chrome()
# driver.get(GOOGLE_TRANSLATE_URL)
# translator = GoogleTranslate(driver)


def get_translated_phrase(translator, language, phrase):
    translator.select_language(language)
    translation = translator.translate_phrase(phrase)
    return translation


def add_translation_to_file(language, translation):
    with open(f'translations-{language}', 'a') as f:
        f.write(translation + '\n')


def translate_phrases_into_languages(phrases, languages):
    driver = webdriver.Chrome()
    driver.get(GOOGLE_TRANSLATE_URL)
    translator = GoogleTranslate(driver)

    for phrase in phrases:
        # translations = []
        for language in languages:
            translation = get_translated_phrase(translator, language, phrase)
            add_translation_to_file(language, translation)
            # translator.select_language(language)
            # translation = translator.translate_phrase(phrase)
            # translations.append(translation)
    driver.quit()


translate_phrases_into_languages(phrases_to_translate, LANGUAGES)

print('PROCESS COMPLETE!')


# translator.select_language(example_language)
# translation = translator.translate_phrase(example_phrase)
# print('TRANSLATION: ', translation)

# translator.clear_phrase()
# sleep(3)

# with open(f'translations-{example_language}', 'w') as f:
#     f.write(translation + '\n')


# when finished
# driver.quit()
