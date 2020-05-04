from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

from IPython.display import Image

import pandas as pd
import numpy as np
import pydotplus
import os

tennis_data = pd.read_csv('/Users/yanghyesun/playtennis.csv')

tennis_data.Outlook = tennis_data.Outlook.replace('Sunny', 0)
tennis_data.Outlook = tennis_data.Outlook.replace('Overcast', 1)
tennis_data.Outlook = tennis_data.Outlook.replace('Rain', 2)
tennis_data.Temperature = tennis_data.Temperature.replace('Hot', 3)
tennis_data.Temperature = tennis_data.Temperature.replace('Mild', 4)
tennis_data.Temperature = tennis_data.Temperature.replace('Cool', 5)
tennis_data.Humidity = tennis_data.Humidity.replace('High', 6)
tennis_data.Humidity = tennis_data.Humidity.replace('Normal', 7)
tennis_data.Wind = tennis_data.Wind.replace('Weak', 8)
tennis_data.Wind = tennis_data.Wind.replace('Strong', 9)
tennis_data.PlayTennis = tennis_data.PlayTennis.replace('No', 10)
tennis_data.PlayTennis = tennis_data.PlayTennis.replace('Yes', 11)
tennis_data

X = np.array(pd.DataFrame(tennis_data, columns = ['Outlook', 'Temperature', 'Humidity', 'Wind']))
y = np.array(pd.DataFrame(tennis_data, columns = ['PlayTennis']))

X_train, X_test, y_train, y_test = train_test_split(X, y)
# 분석 시작
dt_clf = DecisionTreeClassifier()
dt_clf = dt_clf.fit(X_train, y_train) # 데이터 학습
dt_prediction = dt_clf.predict(X_test) # 예측값 계산
dt_prediction
print(confusion_matrix(y_test, dt_prediction)) # 분류평가표, 오차행렬
print(classification_report(y_test, dt_prediction)) # 결과

feature_names = tennis_data.columns.tolist() # ['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis']
feature_names = feature_names[0:4] # ['Outlook', 'Temperature', 'Humidity', 'Wind']
target_name = np.array(['Play No', 'Play Yes'])
dt_dot_data = tree.export_graphviz(dt_clf, out_file = None, 
                                   feature_names = feature_names,
                                   class_names = target_name,
                                   filled = True, rounded = True,
                                   special_characters = True)
dt_graph = pydotplus.graph_from_dot_data(dt_dot_data)
Image(dt_graph.create_png())