def Merhaba(gezegen="Mars",num=0):
    return "Merhaba {}{}".format(gezegen,num)
     

print(Merhaba())

print(Merhaba(num=10))

print(Merhaba("Jupiter"))

for i in range(1,4):
    print(Merhaba("Dunya",i))


