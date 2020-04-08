import numpy as np
import pandas as pd
x = np.arange(2,11)
mylist = x.reshape(3,3)
print(mylist)

x2 = np.zeros((5,5))
y2 = np.arange(5)
mylist = x2 + y2
print(mylist)

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print(df)

excel = pd.read_excel('/Users/yanghyesun/employee.xlsx')
empId=[100,101,102,103,104]
excel.insert(loc=1,column='emp_id',value=empId)
print(excel)