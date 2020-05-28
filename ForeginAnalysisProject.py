import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import csv

#폰트 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

#파일 불러오기 -> list
f=open('/Users/yanghyesun/Downloads/foreign_count_2012.csv',encoding='cp949')
data=csv.reader(f)
data=list(data)

#파일 불러오기 -> DataFrame
df=pd.read_csv('/Users/yanghyesun/Downloads/foreign_count_2012.csv',encoding='cp949', skiprows=[0,0])
name=input("알고 싶은 국적을 입력해주세요: ")


#찾고 싶은 지역 검색
check=False
for row in data:
    if name in row[1]:
        if check:
            woman=list(map(lambda x: -int(x), row[4:]))
        else :
            man=list(map(int,row[4:]))
            check=True

#label 가져오기
label=data[1][4:]

#그래프 그리기
plt.barh(label, woman,color='r', label='여자')
plt.barh(label, man,color='b', label='남자')
plt.legend()
plt.show()