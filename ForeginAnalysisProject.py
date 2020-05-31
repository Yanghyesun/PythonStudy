from sklearn import linear_model
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
import csv

#폰트 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

#파일 불러오기 -> DataFrame
df=pd.read_csv('/Users/yanghyesun/Downloads/foreign_count_2012.csv',encoding='cp949', skiprows=[0,0])



#2014년 2018년 인구 수 차이
def yearCompare():
    f1=open("/Users/yanghyesun/Downloads/foreign_count_2014.csv",encoding='cp949')
    f2=open("/Users/yanghyesun/Downloads/foreign_count_2018.csv",encoding='cp949')
    
    data1 = csv.reader(f1)
    data1 = list(data1)
    data2 = csv.reader(f2)
    data2 = list(data2)
    
    name=input("알고 싶은 국적을 입력해주세요: ")
    count1=np.zeros(13)
    count2=np.zeros(13)
    
    
    #2014년도 검색
    for row in data1:
        if name in row[1]:
            count1=np.add(count1, np.array(list(map(int,row[4:]))))
            
    #2018년도 검색
    for row in data2:
        if name in row[1]:
            count2=np.add(count2, np.array(list(map(int,row[4:]))))
            
    #label 가져오기
    label=data1[1][4:]
    plt.plot(label, count1, label='2014')
    plt.plot(label, count2, label='2018')
    plt.xticks(rotation='vertical')
    plt.legend()
    plt.show()
    
    

#남자/여자 비율 표
def genderRatio():
    #파일 불러오기 -> list
    f=open('/Users/yanghyesun/Downloads/foreign_count_2012.csv',encoding='cp949')
    data=csv.reader(f)
    data=list(data)
    name=input("알고 싶은 국적을 입력해주세요: ")
    #찾고 싶은 지역 검색
    check=False
    for row in data:
        if name in row[1]:
            title=row[1]
            if check:
                woman=list(map(lambda x: -int(x), row[4:]))
            else :
                man=list(map(int,row[4:]))
                check=True
    
    #label 가져오기
    label=data[1][4:]
    
    #그래프 그리기
    plt.title(title)
    plt.barh(label, woman,color='r', label='여자')
    plt.barh(label, man,color='b', label='남자')
    plt.legend()
    plt.show()
    #겹치는 국적은 어떻게 처리할 것인가