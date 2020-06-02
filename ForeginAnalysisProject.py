from sklearn import linear_model
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
import csv

#폰트 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False


#년도별 체류 외국인 변화 예측
def linearPredict():
    datas = []
    for i in range(1,9):
        f = open("/Users/yanghyesun/Downloads/foreign_count_201"+str(i)+".csv",encoding='cp949')
        data = list(csv.reader(f))
        datas.append(int(data[2][3]))
    
    x=list(range(2011,2019))
    
    test_data={'년도':x,
               '인구수':datas}
    test_data=pd.DataFrame(test_data)
    
    linear_regression = linear_model.LinearRegression()
    linear_regression.fit(X = pd.DataFrame(test_data["년도"]), y=test_data["인구수"])
    
    new_year = list(range(2018,2031))
    prediction = linear_regression.predict(X = pd.DataFrame(new_year))
    
    plt.title('년도별 체류 외국인 변화 예측')
    plt.bar(new_year,prediction,color='grey')
    plt.plot(new_year,prediction,color='gold')
    plt.show()


#년도별 체류 외국인 현황 그래프
def yearChange():
    datas = []
    for i in range(1,9):
        f = open("/Users/yanghyesun/Downloads/foreign_count_201"+str(i)+".csv",encoding='cp949')
        data = list(csv.reader(f))
        datas.append(int(data[2][3]))
    
    x=list(range(2011,2019))
    
    plt.title('년도별 국내 체류 외국인 수')
    plt.plot(x,datas,color='gold',marker='.')
    plt.bar(x,datas,color='grey')
    plt.show()
    
    
#2012년 2015년 2018년 특정 국적 인구 수 차이
def yearCompare():
    f1=open("/Users/yanghyesun/Downloads/foreign_count_2012.csv",encoding='cp949')
    f2=open("/Users/yanghyesun/Downloads/foreign_count_2015.csv",encoding='cp949')
    f3=open("/Users/yanghyesun/Downloads/foreign_count_2018.csv",encoding='cp949')
    
    data1 = csv.reader(f1)
    data1 = list(data1)
    data2 = csv.reader(f2)
    data2 = list(data2)
    data3 = csv.reader(f3)
    data3 = list(data3)
    
    name=input("알고 싶은 국적을 입력해주세요: ")
    count1=np.zeros(13)
    count2=np.zeros(13)
    count3=np.zeros(13)
    
    
    #2012년도 검색
    for row in data1:
        if name in row[1]:
            title=row[1]
            count1=np.add(count1, np.array(list(map(int,row[4:]))))
            
            
    #2015년도 검색
    for row in data2:
        if name in row[1]:
            count2=np.add(count2, np.array(list(map(int,row[4:]))))
            
    #2018년도 검색
    for row in data3:
        if name in row[1]:
            count3=np.add(count3, np.array(list(map(int,row[4:]))))
            
    #label 가져오기
    label=data1[1][4:]
    plt.title(title)
    plt.plot(label, count1, label='2012',color='grey')
    plt.plot(label, count2, label='2015',color='gold')
    plt.plot(label, count3, label='2018',color='olivedrab')
    plt.xticks(rotation='vertical')
    plt.legend()
    plt.show()
    


#2018년도 남자/여자 비율 표
def genderRatio():
    #파일 불러오기 -> list
    f=open('/Users/yanghyesun/Downloads/foreign_count_2018.csv',encoding='cp949')
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
    plt.barh(label, woman,color='gold', label='여자')
    plt.barh(label, man,color='grey', label='남자')
    plt.legend()
    plt.show()
    #겹치는 국적은 어떻게 처리할 것인가
