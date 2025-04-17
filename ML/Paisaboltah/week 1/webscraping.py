from bs4 import BeautifulSoup4
import requests

url="http://boston.craigslist.org/search/sof"
response=requests.get(url)
response

data=response.text
data

soup=BeautifulSoup(data,'html.parser')
tags=soup.findall('a')
for tag in tags:
    print(tag.get('href'))