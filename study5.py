import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import csv

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

#파일 읽어오기
f = open('/Users/yanghyesun/201403.csv', encoding="cp949")
f2 = open('/Users/yanghyesun/202003.csv', encoding="cp949")
data = csv.reader(f)
data2 = csv.reader(f2)
next(data)
next(data)
next(data2)
next(data2)
#배열로 저장 
a=[] #201403
b=[] #202003
bars=[]

for row in data:
    bars.append(row[0][:-14])
    a.append(row[1].replace(",",""))
    
for row2 in data2: 
    b.append(row2[1].replace(",",""))

#numpy 변환
first=np.array(a, dtype="int16")
second=np.array(b, dtype="int16")

result = first - second
x_pos = np.arange(len(result))
#파일 닫기
f.close()
f2.close()

#그래프 그리기
plt.bar(x_pos,result)
plt.xticks(x_pos,bars,rotation='vertical')
plt.show()