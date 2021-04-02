from selenium import webdriver
from page import GoogleTranslate
from time import sleep


example_phrase = "youngblood, say you want me back in your life"
example_language = 'spanish'

driver = webdriver.Chrome()

translator = GoogleTranslate(driver)

translator.select_language(example_language)
translation = translator.translate_phrase(example_phrase)
print('TRANSLATION: ', translation)

translator.clear_phrase()
sleep(3)

with open(f'translations-{example_language}', 'w') as f:
    f.write(translation + '\n')


# translator.clear_phrase()


# when finished
driver.quit()
