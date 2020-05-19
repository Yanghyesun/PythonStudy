from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

import pandas as pd
import numpy as np

tennis_data = pd.read_csv('playtennis.csv')
tennis_data

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

gnb_clf = GaussianNB() # Gaussian Naive Bayes 
gnb_clf = gnb_clf.fit(X_train, y_train)
gnb_prediction = gnb_clf.predict(X_test)

my_test=[[1,5,6,8]] # 흐리고, 춥고, 습도가높고, 바람이 약한날 테이스를 칠까?
my_test_result= gnb_clf.predict(my_test)
print(my_test_result)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


print('Confusion Matrix')
print(confusion_matrix(y_test, gnb_prediction))

print('Classification Report')
print(classification_report(y_test, gnb_prediction))

