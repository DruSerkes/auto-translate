from selenium import webdriver
from page import GoogleTranslate
from languages import LANGUAGES

example_phrase = "youngblood, say you want me back in your life"
example_language = 'spanish'

phrases_to_translate = []

with open('phrases.txt', 'r') as f:
    for phrase in f:
        print('phrase: ', phrase)
        phrases_to_translate.append(phrase.rstrip())


print(f'Phrases to translate: {phrases_to_translate}')

driver = webdriver.Chrome()

translator = GoogleTranslate(driver)

translator.select_language(example_language)
translation = translator.translate_phrase(example_phrase)
print('TRANSLATION: ', translation)

translator.clear_phrase()
sleep(3)

with open(f'translations-{example_language}', 'w') as f:
    f.write(translation + '\n')


# when finished
driver.quit()
