dosya = open("deneme.txt","r+")

for i in range(1,5):
    dosya.write("deneme yazi {}\n".format(i))
  
dosya.seek(15)
print(dosya.read(5))
dosya.close()


