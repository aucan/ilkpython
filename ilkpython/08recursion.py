def faktoryel(sayi):
    if sayi==0:
        return 1
    else:
        return sayi*faktoryel(sayi-1)

girdi= int(input("bir sayi giriniz:"))

print(faktoryel(girdi))