import sqlite3
import random
import time

con = sqlite3.connect("deneme.db")

cursor = con.cursor()

def createtable():
    cursor.execute("Create table if not exists denemetable (int id,col1 text,zaman real)")


def insertrows(deger):
    cursor.execute("insert into denemetable values(?,?,?)",(random.randint(1,10),"satir{}".format(deger),time.time())) 
    con.commit()

def showdata():
    cursor.execute("select * from denemetable")
    data= cursor.fetchall()
    return data

createtable()

for i in range(8,9):
    insertrows(i)
    time.sleep(1)

data=showdata()
for i in data:
    print(i[1])

con.close()