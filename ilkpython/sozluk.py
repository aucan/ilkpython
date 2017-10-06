sozluk= {1:"bir",4:"dort",8:"dokuz",9:{6:"alti",7:"yedi",5:["a",12,"c",(3.2,"x")]}}

print(sozluk)

print("---------------")

for i,j in sozluk.items():
    print(i,j )    
print("---------------")

print(sozluk[9][5][3][1])