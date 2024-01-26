# -*- coding: utf-8 -*-
"""day3 and 4 video2 and 3 and 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KIJ8yYj1BtHJwZd3iP9OIZ2V5L772IZE

Linear Regression
"""

import sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
#load_iris(return_X_y = True)
X , y = load_iris(return_X_y = True)
model = LinearRegression()
model.fit(X,y)
model.predict(X)

"""---KNN Regression"""

from sklearn.neighbors import KNeighborsRegressor
mod = KNeighborsRegressor()
mod.fit(X,y)
mod.predict(X)

"""---matplot library"""

import matplotlib.pyplot as plt
pred = mod.predict(X)
plt.scatter(pred,y)

"""Data cleaning and Pre Processing

Plotting
"""

import pandas as pd
from sklearn.datasets import fetch_openml
df = fetch_openml('titanic', version = 1, as_frame = True)['data']
df.info()
df.isnull().sum()
import seaborn as sns
sns.set() #loads seaborn's default theme and colour palette
miss_val_per = pd.DataFrame((df.isnull().sum()/len(df))*100)
miss_val_per.plot(kind = 'bar', title = 'Missing values in percentage', ylabel = 'percentage')

"""---Dropping"""

print("size of dataset = ", df.shape)
df.drop(['body'],axis=1, inplace = True)
print("size of dataset after dropping = ", df.shape)
#miss_val_per = pd.DataFrame(df.isnull().sum()/len(df))*100
#miss_val_per.plot(kind='bar',ylabel='percentage')

"""Value Imputation"""

from sklearn.impute import SimpleImputer
print("No. of null values before imputing",df.age.isnull().sum())
df.age.isnull().sum()
imp = SimpleImputer(strategy = 'mean')
df['age'] = imp.fit_transform(df[['age']])
print("no. of null values after imputing",df.age.isnull().sum())

"""To impute every column's null value"""

def get_parameters(df):
  parameters = {}
  for col in df.columns[df.isnull().any()]:
    if(df[col].dtype == 'int32' or df[col].dtype == 'int64' or df[col].dtype == 'float64'):
      strategy = 'mean'
    else:
      strategy = 'most frequent'
    missing_values = df[col][df[col].isnull()].values[0]
    parameters = {'Missing values': missing_values, 'strategy': strategy}

"""Feature Engineering"""

import pandas as pd
from sklearn.datasets import fetch_openml
df = fetch_openml('titanic', version = 1, as_frame = True)['data']
df['family'] = df['sibsp'] + df['parch']
df.loc[df['family']>0 , 'traveled_alone'] = 0
df.loc[df['family']==0 , 'traveled_alone'] = 1
df['traveled_alone'].value_counts().plot(kind = 'bar', title = 'traveled alone')

"""Data Encoding"""

from sklearn.preprocessing import OneHotEncoder
df['sex'] = OneHotEncoder().fit_transform(df[['sex']]).toarray()
df['sex']

"""Data Scaling - Standard Scaling"""

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_openml
import pandas as pd
df = fetch_openml('titanic', version = 1, as_frame = True)['data']
num_cols = df.select_dtypes(include = ['int64', 'int32', 'float64']).columns
print(num_cols)
en = StandardScaler()
df[num_cols] = en.fit_transform(df[num_cols])
df[num_cols].describe()

"""KNN Classifier"""

from sklearn import datasets
import pandas as pd
data = datasets.load_wine(as_frame = True)
X = data.data
y = data.target
df = pd.DataFrame(X, columns = data.feature_names)
df['wine_class'] = y
df['wine_class'] = df['wine_class'].replace(to_replace = [0,1,2], value = ['class0', 'class1', 'class2'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
import math
#math.sqrt(len(y_test))
knn = KNeighborsClassifier(n_neighbors = 7)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred)