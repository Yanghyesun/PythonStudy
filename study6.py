import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import csv

#폰트 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

#파일 읽어오기
f = open('/Users/yanghyesun/age.csv',encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)
name = input('원하는 지역의 이름을 입력해주세요 : ')

mn=1
result_name=''
result=0

compare=0
for row in data:
    if name in row[0]:
        home = np.array(row[3:],dtype=int) / int(row[2])
        first = row[0]

orderArray=[]
orderName=[]

for i in range(0,4):
    mn=1
    for row in data:
        away= np.array(row[3:],dtype=int) / int(row[2])
        s=np.sum((home-away)**2)
        if s<mn and compare<s and name not in row[0]:
            mn = s
            result_name = row[0]
            result = away
    orderArray.append(result)
    orderName.append(result_name)
    compare = mn

plt.xlabel('나이')
plt.plot(home, label=first)
plt.plot(orderArray[0],label=orderName[0])
plt.plot(orderArray[1],label=orderName[1])
plt.plot(orderArray[2],label=orderName[2])
plt.plot(orderArray[3],label=orderName[3])
plt.legend()
plt.show()