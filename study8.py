import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import csv

#폰트 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

#파일 읽어오기
f = open('/Users/yanghyesun/201903subway.csv', encoding="UTF8")
f2 = open('/Users/yanghyesun/202003subway.csv', encoding="UTF8")
data = csv.reader(f)
data2 = csv.reader(f2)
next(data)
next(data)
next(data2)
next(data2)

a=[]
b=[]

lastOn = [0] * 27 #201903
lastOff = [] 

recentOn = [] #202003
recentOff = []

#콤마 제거 및 숫자 변환
for row in data:
    for i in range(4,len(row)-1):
        row[i] = row[i].replace(",","")
        row[i] = (int(row[i]))
    del(row[0:4])
    del(row[-1])
    a.append(row)
        

for row in data2:
    for i in range(4,len(row)-1):
        row[i] = row[i].replace(",","")
        row[i] = (int(row[i]))
    del(row[0:4])
    del(row[-1])
    b.append(row)

#행끼리 더하기
last = np.sum(np.array(a),axis=0)
recent = np.sum(np.array(b),axis=0)

#승하차 분리
for i in range(0,len(last)):
    if(i%2==0):
        lastOn.append(last[i])
        recentOn.append(recent[i])
    else:
        lastOff.append(last[i])
        recentOff.append(recent[i])

x=np.arange(4,28)
plt.plot(x,lastOn,'b',label='201903승차')
plt.plot(x,lastOff,'y',label='201903하차')
plt.plot(x,recentOn,'g',label='202003승차')
plt.plot(x,recentOff,'r',label='202003하차')
plt.title('지하철 시간대별 승하차 인원 추이(단위 100만명)')
plt.xticks(x)
plt.legend(loc='upper right')
plt.show()