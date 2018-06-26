from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('http://dmce.ac.in').text
soup = BeautifulSoup(source, 'lxml')
title = soup.title.text
print(title)
print('')
for li in soup.body.find_all('li',{'class':'has-dropdown'}) :
    print(li.text)
    for ul in li.ul.find_all('li'):
        href = ul.a.get('href')
        name = ul.text
        print(name)
        print('http://dmce.ac.in'+href)
        print('')
    print('')    

