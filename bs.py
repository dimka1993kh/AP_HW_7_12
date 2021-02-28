from data import url
from bs4 import BeautifulSoup
import requests
strings = []
html_text = requests.get(url)
html_text.raise_for_status()

soup = BeautifulSoup(html_text.text, features="html.parser" )

article = soup.findAll('article', class_='markdown-body')

for el in article:
    code = el.findAll('code')

for el in code:
    strings.append(el.text)