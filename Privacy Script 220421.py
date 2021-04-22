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

############################################
"""
Now let's try the one for UKIP
Pretending to be Mozilla Firefox
"""
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

ukipurl = "https://www.ukip.org/ukip-privacy-policy"

req = Request(ukipurl, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

#parse the html file

page_soup = soup(webpage, "html.parser")

#format the parsed html file
ukippriv = page_soup.prettify()

#print the first few characters
print(ukippriv[:225])

###find the relevant class by checking the HTML
###Found the class that I am interested in: #<div class="dmRespRow"

containers = page_soup.findAll("div", class_ = "dmRespRow")
for container in containers:
    print(container)

#select only the container that I am interested in
ukippolicy = containers[9]
ukippolicy #this container contains the privacy policy.

ukippolicy = page_soup.find_all("p")

clean_ukippolicy = []
for item in ukippolicy:
    item = str(item)
    item = item.replace("<p>", "")
    item = item.replace("</p>", "")
    clean_ukippolicy.append(item)

#make a string out of clean_ukippolicy using list comprehension
clean_ukippolicy_string = ' '.join([str(i) for i in clean_ukippolicy])

##################
"""
Now having a look at Labour
Since you need to accept cookies first before accessing this page
Make sure you pretend to be the browser that you used
to accept the cookies
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

laburl = "https://labour.org.uk/privacy-policy/"

req = Request(laburl, headers={'User-Agent': 'Chrome/74.0.3729.169'})

webpage = urlopen(req).read()

#parse the html file

labour_soup = soup(webpage, "html.parser")

#format the parsed html file
labourpriv = labour_soup.prettify()

#print the first few characters
print(labourpriv[:225])

###find the relevant class by checking the HTML
###Found the class that I am interested in: #<div class="col-xs-12 col-md-8">
	        			
containerslabour = labour_soup.findAll("div", class_ = "col-xs-12 col-md-8")
for container in containerslabour:
    print(container)
    
# and so forth