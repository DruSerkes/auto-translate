from selenium import webdriver
from page import GoogleTranslate


GOOGLE_TRANSLATE_URL = "https://translate.google.com/"

driver = webdriver.Chrome()
driver.get(GOOGLE_TRANSLATE_URL)

translator = GoogleTranslate(driver)
