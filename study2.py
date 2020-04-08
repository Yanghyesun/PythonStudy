import numpy as np
#numpy [1]
a = np.arange(6)
a2 = a[np.newaxis, :]
print(a2.shape)

#numpy [2]
a3 = np.arange(2,9,2)
print(a3)

#numpy [3]
x = np.arange(1,5)
y = np.arange(5,9)
a4 = np.concatenate((x,y),axis=0)
print(a4)

#numpy [4]
a5 = a.reshape(3,2)
print(a5)

#numpy [5]
data = np.array([1,2,3])
a6 = data[1:2]
print(a6)

#numpy [6]
z = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a7 = z[z<5]
print(a7)

#numpy [7]
a8 = np.nonzero(z<5)
print(a8)

#numpy [8]
x1 = np.array([[1,1],[2,2]])
y1 = np.array([[3,3],[4,4]])
a9 = np.vstack((x1,y1))
print(a9)

#numpy [9]
datas = np.array([1,2])
ones = np.ones(2, dtype=int)
a10 = datas+ones
print(a10)

#numpy [10]
a11 = x.sum()
print(a11)