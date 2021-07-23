# -*- coding:utf8 -*-

import csv

# 只能转换utf-8 txt, 需要以','分割
def txt2csv(inputfile,outputfile):  
  datacsv = open(outputfile,'w')  
  csvwriter = csv.writer(datacsv,dialect=("excel"))  
  mainfileH = open(inputfile,'rb')  
  for line in mainfileH.readlines():     
      print "Debug: " + line.replace('\n','')      
      csvwriter.writerow([a for a in line.replace('\n','').split('#')])  
  datacsv.close()  
  mainfileH.close()
 
#注意： 在调用txt2csv之前确认txtfile这个输入文件是close()了的，之前遇到过，如果没有txtfile.close(), 通过readlines读取出来的txtfile文件只有8192 bytes, 后面的字符没被读取到。 还有txtfile中的换行符需要通过 replace替换为'', 否则转化到csv中，每两行之间会有一个空行。 
txt2csv("./application.txt","./application.csv") 