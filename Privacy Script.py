# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 14:09:28 2021

@author: esmer
"""

from requests import get
from bs4 import BeautifulSoup

url = "https://www.conservatives.com/privacy"
response = get(url)

html_soup = BeautifulSoup(response.text, "html.parser")

text = html_soup.find_all("p")

del(text[0:5])
del(text[-1:-5:-1])

clean_text = []
for item in text:
    item = str(item)
    item = item.replace("<p>", "")
    item = item.replace("</p>", "")
    clean_text.append(item)

new_file = open("text7.txt", "w")
new_file.write(str(clean_text))
new_file.close()
