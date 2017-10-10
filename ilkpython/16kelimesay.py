import operator
import requests
from bs4 import BeautifulSoup

def temizle(girdi):
    semboller ="!'+%&/()=?_#${[]}\*-,.~@><|" 
    for sembol in semboller:
        girdi=girdi.replace(sembol,'')
    return girdi
    
    
url="http://www.python.tc/python-nedir/"

tumkelimeler={}

r= requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

for p in soup.find_all("p"):
    icerik= p.text
    kelimeler=icerik.lower().split()
    
    for kelime in kelimeler:
        kelime=temizle(kelime)
        if len(kelime)>0:
            if kelime in tumkelimeler:
                tumkelimeler[kelime]+=1
            else:
                tumkelimeler[kelime]=1

                 
for k,s in  sorted(tumkelimeler.items(),key=operator.itemgetter(1),reverse=True) :
    if s>10 :
        print(k,s)