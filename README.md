# Auto Translator

Translate a list of phrases into a list of languages

## Usage
1. Fork / Clone this repo
2. Install requirements: `pip install -r requirements.txt`  
3. Add the phrases you want to translate to `phrases.txt`
4. Optional: modify the list of languages in `langagues.py`
5. Run from the commmand line `python translate.py` or `python3 translate.py`
6. Take a break while your device does all the heavy lifting
7. Open up the `translations/` sub-directory for your translations when the script has run 

#### Note 
* To avoid installing requirements globally, use a virtual environment: 
  * First use `python -m venv venv` to create a virtual environment
  * Every time you start a new session: `source venv/bin/activate` 
  * Install requirements and run the script from within your safe space 

--- 

## Languages
Any language supported by Google Translate

--- 

## Tech 
* Python 3.9.1
* Selenium 
* Chromedriver-py
* A little help from [Google Translate](https://translate.google.com)
