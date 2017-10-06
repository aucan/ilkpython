#burada for ornegi var

for i in range(3):
    print(i)

print("--------------------")

for i in range(2,6):
    print(i)

print("--------------------")

for i in "deneme":
    print(i)
    
print("--------------------")

liste= ["bir","iki","uc"]

for i in liste:
    print(i)

print("--------------------")

liste= [1,2,3,(3.4,3.8),"dort"]

for i in liste:
    if type(i) !=tuple:
        print(i)
    else:
        tpl= i
        for j in tpl:
            print(j)
    
print("--------------------")

liste= [1,2,3,[3.4,3.8],4]

for i in liste:
    if type(i) not in [list,tuple]:
        print(i)
    else:
        tpl= i
        for j in tpl:
            print(j)
    