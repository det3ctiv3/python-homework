from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time

##1

# chrome_options = Options()
# chrome_options.add_argument("--window_position = -1700, -200")
# driver = webdriver.Chrome(chrome_options)
# driver.get("https://github.com")
#
# print(f"The page title is {driver.title}")

## 2
countries = {}
url = 'https://data.worldbank.org/country'
res = requests.get(url)
soup = BeautifulSoup(res.content, features="html.parser")
sections = soup.find_all('section')
for section in sections:
    title = section.find('h3')
    countries[title.text] = []
    names = section.find_all('a')
    for name in names:
      countries[title.text].append(name.text)

print(countries)

