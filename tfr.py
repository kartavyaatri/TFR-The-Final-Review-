import bs4
import requests
import sys
import re

dataset=open(r'Park_Plaza.txt','w',encoding='utf-8')
for page in range(1,10):
    res=requests.get("https://www.tripadvisor.in/Hotel_Review-g1584814-d6542085-Reviews-or"+str(5*page)+"-Park_Plaza_Zirakpur-Zirakpur_Chandigarh.html")
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.find_all(class_=re.compile('partial_entry'))
    for elem in elems:
        dataset.write(elem.text+'\n')
        print(elem.text)
dataset.close()
