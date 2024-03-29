# -*- coding: utf-8 -*-
"""day5 SVMvid5 and Linearregressionvid6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u4VfvctTqzIcCF5FlEsnOVBCtznOIexv
"""



#importing dataset into dataframe
import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(X, columns = iris.feature_names)
df['species'] = y
df['species'] = df['species'].replace(to_replace = [0,1,2], value = ['setosa','versicolor', 'virginica'])

#spliting training and testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 1)

#implementing Support Vector Machine(SVM)
from sklearn.svm import SVC
svm = SVC(kernel = 'linear', random_state = 0)
svm.fit(X_train, y_train)
pred = svm.predict(X_test)

#finding accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred)

"""Linear Regressor Model"""


import pandas as pd
from sklearn.datasets import load_iris
X,y = load_iris(return_X_y = True)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 1)
from sklearn.linear_model import LinearRegression
mod = LinearRegression()
mod.fit(X_train, y_train)
pred = mod.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred)
