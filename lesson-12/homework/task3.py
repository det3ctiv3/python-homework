from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = 'https://www.demoblaze.com/#'
driver.get(url)
time.sleep(4)

soup = BeautifulSoup(driver.page_source, 'html.parser')
laptops = []

for laptop in soup.find_all('div', class_='card-block'):
    name = laptop.find('a', class_='hrefch').text
    price = laptop.find('h5').text
    desc = laptop.find('p').text
    laptops.append({
        "name": name,
        "price": price,
        "description": desc
    })

driver.quit()
with open("laptops.json", "w") as file:
    json.dump(laptops, file)

