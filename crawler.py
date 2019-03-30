import requests
from bs4 import BeautifulSoup
import urllib.request
link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link)
soup = BeautifulSoup(r.text,"lxml")
# title = soup.find("h1",class_="post-title").a.text.strip()
title = soup.find_all("h1",class_="post-title")
print(title)
list = []
for i in title:
    x = i.find('a').text
    print(x)
