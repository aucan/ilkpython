class calisan:
    def __init__(self, ad,soyad,maas=1000):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas 

    def print(self,ekler=""):
        print("ad:",self.ad,"\tsoyad:",self.soyad,"\tmaas",self.maas,ekler)

class yonetici(calisan):
    def __init__(self, ad, soyad, maas, departman):
        self.departman=departman
        return super().__init__(ad, soyad, maas)

    def print(self): 
        super().print("\tdepartman:{}".format(self.departman))

calisan1= calisan("ali","yilmaz")
calisan2= calisan("veli","celik","2000")
calisan3= calisan("hasan","demir","3000")
yntc = yonetici("haydar","haydi",5000,"ik")

liste=[] 
liste.append(calisan1)
liste.append(calisan2)
liste.append(calisan3) 
liste.append(yntc)  

for clsn in liste:
    clsn.print()    
     