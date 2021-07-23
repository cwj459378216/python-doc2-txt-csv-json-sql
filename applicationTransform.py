# -*- coding:utf8 -*-
import json

jsonT = '{"data":['
for index, line in enumerate(open("./application.txt")):
    if len(line) != 0:
            row = line.strip().split(" ")
            str1 = ''
            for i, r in enumerate(row):
                if len(r) != 0:
                    str1 += r + ','
            if index == 0:
                title = str1.split(',')  
            else: 
                s = str1.split(',')
                j = '{'
                for c, a in enumerate(s):
                    if len(s) - c > 1:
                        if title[c] is '':
                            j += '"' + str(c) + '":"' + a + '",'   # 特殊情况,字段超出
                        else:
                            j += '"' +title[c] + '":"' + a + '",'
                if ',' in j > 0:
                        j = j[0:-1]     
                j += '}'
                jsonT += j +','
if ',' in jsonT > 0:
    jsonT = jsonT[0:-1]                  
jsonT += ']}'
# print jsonT  
# print '---------------------------'
# JSON = json.loads(jsonT)
# print JSON        

new_dict = json.loads(jsonT)
# print new_dict["data"]
with open("./application.sql","w") as f:
    for dict in new_dict["data"]:
        if len(dict) > 0:
            if len(dict) > 5: 
                sql = "insert into settings_application_protocol (id,protocol,layer_4,breed,category) values(%s,'%s','%s','%s','%s');" % (int(dict["Id"]),dict["Protocol"],dict["Layer_4"],dict["Breed"],dict["Category"] + ',' + dict["5"])
            else:
                sql = "insert into settings_application_protocol (id,protocol,layer_4,breed,category) values(%s,'%s','%s','%s','%s');" % (int(dict["Id"]),dict["Protocol"],dict["Layer_4"],dict["Breed"],dict["Category"])
            f.write(sql + '\n')
            print sql

with open("./application.json","w") as f:
    json.dump(new_dict,f)
    print 'json create'
