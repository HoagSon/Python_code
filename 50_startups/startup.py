import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

data = pd.read_csv("50_Startups.csv")
x = np.array(data.iloc[:,0:4].values)
y = np.array(data.iloc[:,-1].values)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(x[0:,3])
x[0:,3] = le.transform(x[0:,3])

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=0)

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

y_pred = lin_reg.predict(x_test) 

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print("r2:",r2)

