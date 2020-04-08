import pandas as pd
import numpy as np
#pandas [1]
a1=pd.Series([1,3,5,np.nan,6,8])
print(a1)

#pandas [2]
a2 = pd.DataFrame({'A':1.,
'B':pd.Timestamp('20200405'),
'C':pd.Series(1, index=list(range(4)),dtype='float32'),
'D':np.array([3] * 4,dtype='int32'),
'E':pd.Categorical(["test","train","test","train"]),
'F':'foo'})
print(a2)

#pandas [3]
print(a2.dtypes)
print(a2.index)
print(a2.columns)

#pandas [4]
a3 = pd.DataFrame(np.random.randn(5,4),columns=['A','B','C','D'])
print(a3)
print(a3.describe())
print(a3['A'])

#pandas [5]
a4 = a3.loc[:, ['A','B']]
print(a4)

#pandas [6]
a5 = a3.iloc[0]
a6 = a3.iloc[2]
print(a5)
print(a6)

#pandas [7]
dates=['20200401','20200402','20200403','20200404','20200405','20200406']
a7 = pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
print(a7)

#pandas [8]
a8 = pd.Series(['A','B','C','Aaba','Baca',np.nan,'CABA','dog','cat'])
print(a8.str.lower())

#pandas [9]
left = pd.DataFrame({'key': ['foo','foo'],'lval':[1,2]})
right = pd.DataFrame({'key': ['foo','foo'],'rval':[4,5]})
a9 = pd.merge(left,right, on='key')
print(a9)

#pandas [10]
a10 = pd.DataFrame({'A':['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
'B':['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
'C': np.random.randn(8),
'D': np.random.randn(8)})
print(a10.groupby('A').sum())