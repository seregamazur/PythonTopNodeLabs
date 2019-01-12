#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib.request, json

file = open("result.csv",'w')
response = requests.get('http://www.codeabbey.com/index/user_ranking')

page_content = BeautifulSoup(response.content, "html.parser")
result = page_content.find_all('tr')

with urllib.request.urlopen("https://api.seller.rozetka.com.ua/items/id") as url:
    data = json.loads(url.read().decode())
    print(data)
#file.write("Position,Username,Language,Rank,Enlightenment,Solved\n")
#for tr in result[2:]:
 #       td = tr.findAll('td')
  #      file.write(td[0].text)
   #     file.write(',')
    #   file.write(',')
     #   file.write(td[3].text)
      #  file.write(',')
       # file.write(td[4].find('span').text)
        #file.write(',')
        #file.write(td[5].text.replace(',', '.'))
        #file.write(',')
        #file.write(td[6].text)
        #file.write('\n')

