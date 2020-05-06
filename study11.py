from sklearn.datasets import load_iris
#from sklearn import tree
#import numpy as np
from sklearn.metrics import accuracy_score
import pandas as pd
#loading the iris dataset
iris = load_iris()

# to excel... by Uchang
df = pd.DataFrame(data=iris['data'], columns = iris['feature_names'])
df['target']=iris.target
df.to_excel('iris.xlsx', index=False)

from sklearn.model_selection import train_test_split
x = iris.data
y = iris.target
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2)

# Initialize the model
clf_2 = RandomForestClassifier(n_estimators=200, # Number of trees
                               max_features=4,    # Num features considered
                               oob_score=True)    # Use OOB scoring*
clf_2.fit(X_train, Y_train)
prediction_2 = clf_2.predict(X_test)
myX_test=np.array([[5.6,2.9,3.6,1.3]])
myprediction = clf_2.predict(myX_test)
print ("Accuracy is : ",accuracy_score(prediction_2, Y_test))
print ("=======================================================")
print (classification_report(prediction_2, Y_test))
print(myprediction)

# 각 속성의 중요도 출력 petal length?
for feature, imp in zip(iris.feature_names, clf_2.feature_importances_):
    print(feature, imp)
    
from IPython.display import Image
import pydotplus
model = clf_2.estimators_[5]
feature_names = iris.feature_names[0:4]
target_name = np.array(['iris1', 'iris2','iris3'])
dt_dot_data=tree.export_graphviz(model,
feature_names = iris.feature_names, class_names = iris.target_names, filled = True, rounded = True, special_characters = True)
dt_graph = pydotplus.graph_from_dot_data(dt_dot_data)
Image(dt_graph.create_png())