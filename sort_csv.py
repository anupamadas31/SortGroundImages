import csv
from operator import itemgetter

# with open('‪C:\Users\hcilab\Desktop\sort.csv')
          # 'C:\Users\Anapuma\Desktop\sort.csv', 'r') as f:
    # data = [line for line in csv.reader(f)]


# data.sort(key=itemgetter(1))  # 1 being the column number
# result = df.sort(['name'], ascending=[1, 0])

# with open('C:\Users\Anapuma\Desktop\sort.csv', 'w') as f:
#     csv.writer(f).writerows(data)

import sys, csv ,operator
import pandas as pd

df =pd.read_csv(r'D:\CARINATA\B2\7JUNE\r67\distib.csv')
filenames= df['filename']
flags=[]
turns=[]
path=''
for file in filenames:
    filepath= file.split('/')
    lastchar= filepath[-1]

    number= lastchar[lastchar.find("(") + 1:lastchar.find(")")]
    # print(lastchar.split(' ')[0])
    if (lastchar.split(' ')[0]=='flag'):
        path=file.split('flag')[0]
        flags.append(int(number))
    elif (lastchar.split(' ')[0]=='turn'):
        turns.append(int(number))

# print(len(flags))
# print(len(turns))

import numpy as np
flags= np.sort(flags)
turns=np.sort(turns)

# print(len(flags))
# print(len(turns))

turnpaths=[]
flagpaths=[]

for each in flags:
    flagpaths.append(path+'flag ('+str(each)+').JPG')

for each in turns:
    turnpaths.append(path+'turn ('+str(each)+').JPG')

indexs=[]
for each in flagpaths:
   indexs.append(df.index[df.filename==each][0])
for each in turnpaths:
   indexs.append(df.index[df.filename==each][0])

outputdf= df.reindex(indexs)
outputdf.to_csv(r'D:\CARINATA\B2\7JUNE\r67\distib_sorted.csv')
print(outputdf)
# print(filenames)




# sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
#
#
# # #now write the sorte result into new CSV file
# with open(r'D:\CARINATA\B2\7JUNE\r57\new-distib.csv', 'r') as f:
#     csv.writer(f).writerows(sortedlist)

