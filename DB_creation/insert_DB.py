import json
import sqlite3 as sqlite
import re
connection = sqlite.connect('RusDict.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE Sources(
Id INTEGER,
Lower TEXT,
Name TEXT,
Sokr TEXT,
Pusto TEXT,
Time1 TEXT,
Time2 TEXT,
Bib TEXT,
Gomilet TEXT,
Bog TEXT,
Agiogr TEXT,
Pov TEXT,
Litur TEXT,
Epi TEXT,
Letop TEXT,
Hron TEXT,
Docum TEXT,
Lang TEXT,
Bib1 TEXT,
Gom1 TEXT,
Bog1 TEXT,
Agiogr1 TEXT,
Pov1 TEXT,
Litur1 TEXT,
Epi1 TEXT,
Hron1 TEXT,
Docum1 TEXT
);
''')

f = open('merged.json','r',encoding='utf-8')

f1 = open('test3.csv','w',encoding='utf-8')
d = ''
for i in f:
    d+=i
arr = json.loads(d)
co = 0
for e in arr:
    print(co)
    co+=1
    try:
        sql = 'INSERT INTO Sources VALUES(' + str(e)+", '"+arr[e][0].lower()+"'"
    except:
        sql = 'INSERT INTO Sources VALUES(' + str(e)+", ''"
    if len(arr[e]) < 25:
        ar = arr[e] + ['']*(25-len(arr[e]))
    else:
        ar = arr[e][0:25]
    for b in ar:
        d = re.sub("\'","",d)
        d = re.sub('\"',"",d)
        sql += ",'" + b + "'"
    sql+=')'
    #print(sql)
    cursor.execute(sql)
connection.commit()
f1.close()
f.close()

