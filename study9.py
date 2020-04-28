from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {'x' : [59, 49, 75, 54, 78, 56, 60, 82, 69, 83, 88, 94, 47, 65, 89, 70],
'y': [209, 180, 195, 192, 215, 197, 208, 189, 213, 201, 214, 212, 205, 186, 200, 204]}
data = pd.DataFrame(data)
data.plot(kind='scatter',x='x', y='y', figsize=(5,5), color='black')

linear_regression = linear_model.LinearRegression()
linear_regression.fit(X = pd.DataFrame(data["x"]), y=data["y"])

prediction = linear_regression.predict(X = pd.DataFrame(data["x"]))
print(linear_regression.intercept_)
print(linear_regression.coef_)

residuals = data["y"] - prediction
print(residuals)

SSE = (residuals**2).sum()
SST = ((data["x"]-data["y"].mean())**2).sum()

R_squared = 1-(SSE/SST)

plt.plot(data["x"],prediction,color="blue")
print(R_squared)

print(linear_regression.predict(X=pd.DataFrame([58])))