import requests
from bs4 import BeautifulSoup
r= requests.get("http://www.imdb.com/chart/top")
soup=BeautifulSoup(r.content,"html.parser")
gelenveri=soup.find_all("table",{"class":"chart full-width"})

filmler=gelenveri[0].contents[5].find_all("tr")
filmisimleri=[]
for x in filmler:
    filmisimleri.append(x.find_all("td",{"class":"titleColumn"})[0].text.replace('\n','').replace('\t',''))    
print(filmisimleri[0])