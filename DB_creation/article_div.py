import re
import sqlite3 as sqlite
import json

def roman2arabic(roman):
    digit = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    arabic = 0
    for d in range(len(roman)):
        try:
            if digit[roman[d]]<digit[roman[d+1]]:
                arabic-=digit[roman[d]]
            else:
                arabic+=digit[roman[d]]
        except IndexError:
            arabic+=digit[roman[d]]
    return arabic

def fa(string, st):
    numchar = 0
    finaut = {}
    finaut[(0,'<')]=1 #begining
    finaut[(1,'i')]=2 #inside id-tag
    finaut[(2,'d')]=3 #inside id-tag
    finaut[(3,'=')]=4 #inside id-tag
    finaut[(4,'1')]=5 #id-num
    finaut[(4,'2')]=5 #id-num
    finaut[(4,'3')]=5 #id-num
    finaut[(4,'4')]=5 #id-num
    finaut[(4,'5')]=5 #id-num
    finaut[(4,'6')]=5 #id-num
    finaut[(4,'7')]=5 #id-num
    finaut[(4,'8')]=5 #id-num
    finaut[(4,'9')]=5 #id-num
    finaut[(5,'1')]=5 #id-num
    finaut[(5,'2')]=5 #id-num
    finaut[(5,'3')]=5 #id-num
    finaut[(5,'4')]=5 #id-num
    finaut[(5,'5')]=5 #id-num
    finaut[(5,'6')]=5 #id-num
    finaut[(5,'7')]=5 #id-num
    finaut[(5,'8')]=5 #id-num
    finaut[(5,'9')]=5 #id-num
    finaut[(5,'0')]=5 #id-num
    finaut[(5,'>')]=6 #id-tag fin
    finaut[(6,'<')]=7 #bold-tag
    finaut[(7,'b')]=8 #bold-tag
    finaut[(8,'>')]=9 #bold-tag fin
    ident = ''
    ident_final = ''
    for i in string:
        numchar+=1
        if (st, i) in finaut:
            st = finaut[(st,i)]
            if st == 5:
                ident+=i
            if st == 6:
                ident_final = ident
                ident = ''
            if st == 9:
                return [ident_final,st,numchar]


def wordfa(string,numchar):
    st = 9
    bigletters = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮѢ'
    faw = {}
    numchar1 = numchar
    faw[(9, '<')] = 10
    faw[(10, '/')] = 11
    faw[(11, 'b')] = 12
    faw[(12, '>')] = 13
    word = ''
    for i in string[numchar:]:
        numchar1+=1
        if (st,i) not in faw:
            word+=i
        else:
            st = faw[(st,i)]
            if st == 13:
                return([word,st,numchar1])
def wordfa1(string,numchar):
    bigletters = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮѢ,. '
    st = 0
    numchar1 = numchar
    faw = {}
    faw[(0,',')]=0
    faw[(0,' ')]=0
    faw[(0,'<')]=0
    faw[(0,'/')]=14
    faw[(14,'i')]=15
    faw[(15,'>')]=0
    faw[(0,'и')]=1
    faw[(1,'л')]=13
    faw[(13,'и')]=1
    faw[(0,'ч')]=10
    faw[(10,'а')]=11
    faw[(11,'щ')]=12
    faw[(12,'е')]=1
    faw[(1,' ')]=1
    faw[(1,'<')]=2
    faw[(2,'b')]=3
    faw[(3,'>')]=4
    faw[(5,'<')]=6
    faw[(6,'/')]=7
    faw[(7,'b')]=8
    faw[(8,'>')]=9
    fw = ''
    for i in string[numchar:]:
        numchar1+=1
        if (st,i) not in faw and st != 4 and st !=5:
            return(None)
        if (st,i) in faw:
            st = faw[(st,i)]
        if st == 5:
            fw+=i
        if st == 4:
            st = 5
        if st == 9:
            return([fw,numchar1])

def gram(string,numchar):
    st = 13
    numchar1 = numchar
    dic = {}
    dic[(13,'и')]=13
    dic[(13,'/')]=13
    dic[(13,'i')]=13
    dic[(13,'>')]=13
    dic[(13,'<')]=13
    dic[(13,',')]=13
    dic[(13,' ')]=13
    dic[(13,'.')]=13
    dic[(13,'с')]=44
    dic[(44,'м')]=48
    dic[(13,'<')]=15
    dic[(15,'i')]=16
    dic[(16,'>')]=17
    dic[(17,' ')]=17
    dic[(17,'м')]=18
    dic[(18,'н')]=44
    dic[(17,'с')]=18
    dic[(17,'ж')]=18
    dic[(17,'п')]=21
    dic[(18,'е')]=22
    dic[(22,'с')]=23
    dic[(23,'т')]=24
    dic[(17,'п')]=21
    dic[(21,'р')]=22
    dic[(22,'е')]=35
    dic[(35,'д')]=36
    dic[(36,'л')]=37
    dic[(37,'о')]=38
    dic[(38,'г')]=39
    dic[(22,'и')]=23
    dic[(23,'л')]=24
    dic[(23,'ч')]=43
    dic[(17,'н')]=25
    dic[(25,'а')]=26
    dic[(26,'р')]=27
    dic[(27,'е')]=28
    dic[(28,'ч')]=29
    dic[(18,'о')]=30
    dic[(30,'ю')]=31
    dic[(31,'з')]=32
    dic[(17,'ч')]=33
    dic[(33,'а')]=34
    dic[(34,'с')]=35
    dic[(35,'т')]=36
    dic[(36,'и')]=37
    dic[(37,'ц')]=38
    dic[(38,'а')]=39
    dic[(33,'и')]=40
    dic[(40,'с')]=41
    dic[(41,'л')]=42
    dic[(18,'<')]=19
    dic[(24,'<')]=19
    dic[(29,'<')]=19
    dic[(32,'<')]=19
    dic[(39,'<')]=19
    dic[(42,'<')]=19
    dic[(43,'<')]=19
    dic[(44,'<')]=19
    dic[(19,'/')]=19
    dic[(19,'i')]=19
    dic[(19,'>')]=19
    dic[(18,'.')]=20
    dic[(19,'.')]=20
    dic[(24,'.')]=20
    dic[(29,'.')]=20
    dic[(32,'.')]=20
    dic[(39,'.')]=20
    dic[(39,' ')]=39
    dic[(42,'.')]=20
    dic[(43,'.')]=20
    dic[(44,'.')]=20
    word =''
    for i in string[numchar:]:
        if (st,i) in dic:
            st = dic[(st,i)]
            if st <= 44:
                numchar1+=1
            if st == 18 or st >= 21 and st <=44:
                word+=i
            if st == 20:
                if word == '':
                    return(['глаг',numchar1])
                else:
                    return([word,numchar1])
            if st ==48:
                return(None)
        else:
            return(['глаг',numchar1])


def meanings(string,numchar):
    meanings = string[numchar:].split('</p><p>')
    return(meanings)

def links(string,numchar):
    st = 0
    d = re.search('( )?см\.( )?<b>.+?</b>',string[numchar:])
    if d is not None:
        return([d.group(0),numchar])

def examplesdev(string):
    string = re.sub('(<)(/)?[pib]>','',string)
    string = re.sub('([XVI1642357890]+? (в(в)?|г(г)?)\.( ~ [1642357890XVI]+? (г(г)?|в(в)?)\.)?)','\\1@',string)
    arr = string.split('@')
    return(arr)

def finfu(string):
    finalstring = ''
    finarr = []
    numchar = 0
    ident = fa(string,numchar)
    finarr.append(ident)
    if ident is not None:
        numchar = ident[2]
    word1 = wordfa(string, numchar)
    finarr.append(word1)
    if word1 is not None:
        numchar = word1[2]
    gram1 = gram(string,numchar)
    finarr.append(gram1)
    if gram1 is not None:
        numchar = gram1[1]
    word2 = wordfa1(string,numchar)
    finarr.append(word2)
    if word2 is not None:
        numchar = word2[1]
    gram2 = gram(string,numchar)
    finarr.append(gram2)
    if gram2 is not None:
        numchar = gram2[1]
    link = links(string,numchar)
    finarr.append(link)
    if link is not None:
        numchar = link[1]
    for i in finarr:
        if i is not None:
            finalstring+=i[0]+'\t'
        else:
            finalstring+='NULL\t'
    if ident is None:
        ident = 'NULL'
    else:
        ident = ident[0]
    if word1 is None:
        word1 = 'NULL'
    else:
        word1 = word1[0]
    if gram1 is None:
        gram1 = 'NULL'
    else:
        gram1 = gram1[0]
    if word2 is None:
        word2 = 'NULL'
        gram2 = None
    else:
        word2 = word2[0]
    if gram2 is None or gram2 == 'глаг':
        gram2 = 'NULL'
    else:
        gram2 = gram2[0]
    if link is None:
        link = 'NULL'
    else:
        link = re.sub('(( )?см\.( )?<b>|</b>)','',link[0])
    
    meanings1 = meanings(string,numchar)
    meaningID = 1
    full = ''
    for i in meanings1:
        meaningID+=1
        d = re.search('<?i?>?.*?</i>(\))?((\.)?( )?<b>.*?</b>)?(( )?(\()?( )?<i>( )?(\()?( )?в знач( )?(\.)?( )?</i>( )?(\.)?( )?[1234567890]( ?)(;|\.)?( )?(\))?)?((\.)?( )?[^ ]+?\))?((\\.)?( )?[1234567890](\.|;)?)?(( )?(\()?( )?<i>ср\\. [^ ]+?</i>( )?(\\.)?( )?[^ ]+( )?([^ ])?(( )?<i>в этом знач</i>(\.)?)?(( )?(‘)?<i>(‘)?\w+?(’)?</i>(‘)?)?(\))?)?(( )?<i>\w+?( \w+?)?(\w+?)?</i>(\.)?)?',i)
        #d = re.search('<?i?>?.*?</i>((\.)?( )?<b>.*?</b>)?(( )?(\()?( )?<i>( )?(\()?( )?в знач( )?(\.)?( )?</i>( )?(\.)?( )?[1234567890]( ?)(;|\.)?( )?(\))?)?(( )?[^ ]+?\))?((\\.)?( )?[1234567890](\.|;)?)?(( )?<i>ср\\. [^ ]+?</i>\\. [^ ]+?\))?',i) . stwierdzić się ‘<i>осуществиться’</i>)
        if d is not None:
            me = re.sub('<(/)?[IiBb]>', '', d.group(0))
            query1 = "INSERT INTO Meanings VALUES(NULL, '" + me+"', " + ident+")"
            me1 = re.sub('(<)?(/)?i>', '', me)
            me1 = re.sub('&SUP&', ' ', me1)
            me1 = re.sub('&sup&', ' ', me1)
            full += '%&'+me1+'&'
            cursor.execute(query1)
            query2 = "SELECT Id FROM Meanings WHERE rowid=last_insert_rowid();"
            cursor.execute(query2)
            t = cursor.fetchall()
            meaningid = t[0][0]
            arrex = examplesdev(i[len(d.group(0)):len(i)])
            for x in arrex:
                x = re.sub("(\'|\")",'',x)
                #query3 = "INSERT INTO Examples VALUES(NULL, '" + x + "', " + str(meaningid)+")"
                #cursor.execute(query3)
                dat_source = re.search('(([ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ][ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбю\.])*?(((№\s|(\.|,)(\s)?)[1234&567890йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm\.,]{1,7}(\.|,|\.,)?\s|№\s)*?[ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбюQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm\.,]{2,}(\s[VXI,]+?)?\s[1234567890\.]+?)?(\s)?)(([XVI1642357890]+?((\s)?(~|–)(\s)?))?[XVI1642357890]+?\s(в(в)?|г(г)?)\.((\s)?(~|–)(\s)?[1642357890XVI]+?\s(г(г)?|в(в)?)\.)?|[XVI1642357890]+?(\s)?((в(в)?|г(г)?)\.)?(\s)?(~|–)(\s)?[1642357890XVI]+?(г(г)?|в(в)?)\.)',x)
                #if dat_source is not None:
                    #print(dat_source.group(0))
                dat = re.search('(([XVI1642357890]+?((\s)?(~|–)(\s)?))?[XVI1642357890]+?\s(в(в)?|г(г)?)\.((\s)?(~|–)(\s)?[1642357890XVI]+?\s(г(г)?|в(в)?)\.)?|[XVI1642357890]+?(\s)?((в(в)?|г(г)?)\.)?(\s)?(~|–)(\s)?[1642357890XVI]+?(г(г)?|в(в)?)\.)',x)
                if dat_source is not None:
                    ds = dat_source.group(1)
                    ds = re.sub('^(\s)?(\.|,)(\s)?','',ds)
                    ds = re.sub('^\s','',ds)
                    if len(ds) > 0:
                        if ds not in arr_sou:
                            arr_sou.append(ds)
                        fi.write(ds+'\n')
                        ds = re.sub('<i>', '', ds)
                    date = dat.group(0)
                    date = re.sub('г', '', date)
                    date = re.sub('в', '', date)
                    date = re.sub('\s', '', date)
                    date = re.sub('\.', '', date)
                    datea = date.split('~')
                    if len(datea) == 1:
                        datea.append(datea[0])
                    dateaa = []
                    for i in datea:
                        i = i.split('–')
                        if len(i) == 1:
                            i.append(i[0])
                        for e in i:
                            dateaa.append(e)
                    if 'X' in dateaa[0] or 'V' in dateaa[0] or 'I' in dateaa[0]:
                        dateaa[0] = str(roman2arabic(dateaa[0]))
                    if 'X' in dateaa[1] or 'V' in dateaa[1] or 'I' in dateaa[1]:
                        dateaa[1] = str(roman2arabic(dateaa[1]))
                    if 'X' in dateaa[2] or 'V' in dateaa[2] or 'I' in dateaa[2]:
                        dateaa[2] = str(roman2arabic(dateaa[2]))
                    if 'X' in dateaa[3] or 'V' in dateaa[3] or 'I' in dateaa[3]:
                        dateaa[3] = str(roman2arabic(dateaa[3]))
                                
                    da = dateaa[0] + ", " + dateaa[1] + ", " + dateaa[2] + ", " + dateaa[3] 
                    if ds in list_s:
                        query3 = "INSERT INTO Examples VALUES(NULL, '" + x + "', '" + str(list_s[ds]) + "', " + da + ", " + str(meaningid)+")"
                    else:
                        query3 = "INSERT INTO Examples VALUES(NULL, '" + x + "', '" + '' + "', " + da + ", " + str(meaningid)+")"

        
                    cursor.execute(query3)
                else:
                    if dat is not None:
                        query3 = "INSERT INTO Examples VALUES(NULL, '" + x + "', '" + 'NULL' + "', " + da + ", " + str(meaningid)+")"
 
                        cursor.execute(query3)
                    else:
                        query3 = "INSERT INTO Examples VALUES(NULL, '" + x + "', '" + 'NULL' + "', " + "NULL, NULL, NULL, NULL" + ", " + str(meaningid)+")"

                        cursor.execute(query3)
                x = re.sub('&SUP&', ' ', x)
                x = re.sub('&sup&', ' ', x)
                x = re.sub('(<)?(/)?i>', '',x)
                full += x
    word1 = re.sub('&SUP&', ' ', word1)
    word2 = re.sub('&SUP&', ' ', word2)
    word1 = re.sub('&sup&', ' ', word1)
    word2 = re.sub('&sup&', ' ', word2)
    word1 = re.sub(',', '', word1)
    word2 = re.sub(',', '', word2)
    word1 = re.sub('^\s', '',word1)
    word1 = re.sub('\s$', '',word1)
    word1 = re.sub('\.', '',word1)
    word2 = re.sub('^\s', '',word2)
    word2 = re.sub('\s$', '',word2)
    word2 = re.sub('\.', '',word2)
    query = "INSERT INTO Words VALUES(" + ident + ", '" + word1 + "', '" + gram1 + "', '" + word2 + "', '" + gram2 + "', '" + link + "', '"+ full + "')"
    cursor.execute(query)
    return(finalstring)

connection = sqlite.connect('RusDict.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE Words(
Id INTEGER,
Word1 TEXT,
Gram1 TEXT,
Word2 TEXT,
Gram2 TEXT,
Link TEXT,
Full TEXT
);
''')

cursor.execute('''
CREATE TABLE Meanings(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Def TEXT,
IDword INTEGER
);
''')

cursor.execute('''
CREATE TABLE Examples(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
example TEXT,
source TEXT,
date1 INTEGER,
date2 INTEGER,
date3 INTEGER,
date4 INTEGER,
meaningID TEXT
);
''')
file1 = open('test2.json','r',encoding='utf-8')
j = ''
for i in file1:
    j+=i
list_s = json.loads(j)
arr_sou = []
#print(gram(' <i>ж. Ласк.',0))
fi = open('test.txt', 'w', encoding='utf-8')
file = open('fi.html', 'r', encoding='utf-8')
word = ''
val=0
f = open('res.csv', 'w', encoding='utf-8')
for i in file:
    if i is not None and len(i)>1 and fa(i,0) is not None:
        i = i[0:len(i)-1]
        finfu(i)
        #f.write(finfu(i)[:len(finfu(i))]+'\n')
#    if i is not None and len(i)>1 and fa(i,0) is not None:
#        f.write(str(fa(i, 0)[0])+' | '+str(wordfa(i,fa(i,0)[2])[0])+' | '+str(gram(i,wordfa(i,fa(i,0)[2])[2])[0])+'\n')
f.close()
file.close()
fi.close()
connection.commit()
count = 1
arr_sou_id = []
for i in arr_sou:
    arr_sou_id.append({i: count})
    count += 1
file2 = open('1.json','w',encoding='utf-8')
kf = json.dumps(arr_sou_id, ensure_ascii=False, indent = 2)
file2.write(kf)
file1.close()
