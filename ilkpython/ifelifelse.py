vize= int(input("vize notunu girin:"))
final = int(input("final notunu girin:"))
ortalama = 0.4*vize+0.6*final
if ortalama>=90:
    harf="A"
elif ortalama>=80:
    harf="B"
elif ortalama>=70:
    harf="C"
else :
    harf="F"
print("Ders ortalamaniz:{}".format(harf))