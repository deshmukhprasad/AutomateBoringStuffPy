import csv 
import os

def head(add) :
    newd = []
    filer = open(add)
    filero = csv.reader(filer)
    print('df')
    for row in filero :
        if filero.line_num == 1:
            continue
        else:
            newd.append(row)    
    filer.close()
    filew = open(add , 'w' , newline = '')
    filewo = csv.writer(filew)
    for row in newd :    
        filewo.writerow(row)
    filew.close()

dir = input('Enter the dir\n')
for f in os.listdir(dir) :
    filename , fileext = os.path.splitext(f)
    if fileext == '.csv' :
        head(dir+'\\'+f)

