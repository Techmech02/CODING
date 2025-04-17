import pandas as pd
from sklearn import linear_model
df=pd.read_csv("data.csv")
X=df[['weight','volume']]
y=df['co2']
regres=linear_model.LinearRegression()
regres.fit(X,y)
pdco2=regres.predict([[3300,1300]])
print("Coefficient: ",regres.coef_)