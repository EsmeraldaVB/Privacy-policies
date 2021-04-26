# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:03:48 2021

@author: Eleni, Rachel, Maria and Esmeralda
"""

#UKIP URL = https://www.ukip.org/ukip-privacy-policy
#Labour party URL = "https://labour.org.uk/privacy-policy/
#Britain First URL = "https://www.britainfirst.org/privacy-policy"
#Conservative URL = "https://www.conservatives.com/privacy"

import requests
from bs4 import BeautifulSoup
import re
URL = str(input("enter the URL of the website you want to scrape: "))
page = requests.get(URL, headers={'User-Agent': 'Chrome/74.0.3729.169'})
# print(page.text) if I want to print the response


result_soup = BeautifulSoup(page.text, 'html.parser')
print(result_soup.prettify())
text = result_soup.find_all("p")
bulletpoints = result_soup.find_all("li")
tableinfo = result_soup.find_all("tr")

#remove all html tags i.e. anything that starts with “<“ and ends with “>”
#I have imported re, which is a module for regular expressions
clean_text = []
for item in text:
    item = str(item)
    item = re.compile(r'<[^>]+>').sub('',item)
    clean_text.append(item)

clean_bulletpoints =[]
for point in bulletpoints:
    point = str(point)
    point = re.compile(r'<[^>]+>').sub('',point)
    clean_bulletpoints.append(point)

#The UKIP Privacy Policy has no tables######################################
clean_tableinfo = []
for info in tableinfo:
    info = str(info)
    info = re.compile(r'<[^>]+>').sub('',info)
    clean_tableinfo.append(info)
##############################################################################

final_clean_text = []
#unwanted_chars = ['\n', '\t', 'r', '\xa0', 'â\x80\x93' etc]
#clearly, there is a lot or repetition here; I should try to use a for loop instead
#also each website has its own unwanted characters and it is hard to predict what you will find in the scrapped text
#the user has to check the output to find any new characters and add the relevant line to replace them
for item in clean_text:
    item = str(item)
    item = item.replace("â\x80\x93", "")
    item = item.replace("â\x80\x99", "")
    item = item.replace("\n", "")
    item = item.replace("â\x80\x98", "")
    item = item.replace("â\x80\x9c", "")
    item = item.replace("â\x80\x9d", "")
    item = item.replace("â\x80\x8d", "")
    item = item.replace("Â\xa0", "")
    item = item.replace("\r", "")
    item = item.replace("\xa0", "")
    item = item.replace("&amp", "&")
    final_clean_text.append(item)

final_clean_bulletpoints =[]
for item in clean_bulletpoints:
    item = str(item)
    item = item.replace("â\x80\x93", "")
    item = item.replace("â\x80\x99", "")
    item = item.replace("\n", "")
    item = item.replace("â\x80\x98", "")
    item = item.replace("â\x80\x9c", "")
    item = item.replace("â\x80\x9d", "")
    item = item.replace("â\x80\x8d", "")
    item = item.replace("Â\xa0", "")
    item = item.replace("\r", "")
    item = item.replace("\xa0", "")
    item = item.replace("&amp", "&")
    final_clean_bulletpoints.append(item)

###################################### BF, UKIP and Labour don't have a table
final_clean_tableinfo = []
for item in clean_tableinfo:
    item = str(item)
    item = item.replace("â\x80\x93", "")
    item = item.replace("â\x80\x99", "")
    item = item.replace("\n", "")
    item = item.replace("â\x80\x98", "")
    item = item.replace("â\x80\x9c", "")
    item = item.replace("â\x80\x9d", "")
    item = item.replace("â\x80\x8d", "")
    item = item.replace("Â\xa0", "")
    item = item.replace("\r", "")
    item = item.replace("\xa0", "")
    item = item.replace("&amp", "&")
    final_clean_tableinfo.append(item)
##############################################################################

#joining the separate lists so the whole privacy policy of the website appears as one list that can be compared to another
full_privacy_policy = final_clean_text + final_clean_bulletpoints + final_clean_tableinfo

################
#Time to check the privacy policy text to see how Labour diverts from Conservatives:
print(full_privacy_policy)
#there are no weird characters left in the text
    
#save the full privacy policy as a text file to allow further analysis
#ask the user to name the file, otherwise everytime the user runs the code the file will be replaced
file_name = str(input("enter the name of the new file in which the privacy policy of the website will be saved: "))
new_file = open(file_name+".txt", "w")
#example: new_file = open('privacypolicyukip.txt', 'w')
new_file.write(str(full_privacy_policy))
new_file.close()

##############################################################################
"""
Identify URLS
"""

[w for w in tokenized_word if w.startswith('GDPR')]

