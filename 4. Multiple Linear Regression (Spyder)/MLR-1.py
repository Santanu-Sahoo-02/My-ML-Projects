

# MLR model
# y=m1x1+m2x2+m3x3+...+b
# m1,m2,m3...quotients,b-intercepts

#homeprises.csv - 
#also predict for a. 3000 sqft area, 3 bed rooms, 40 years old
# b. 2500 sqft area, 4 bed rooms, 5 years old
#price=m1*area+m2*bedrooms+m3*age+b
import pandas as pd
df=pd.read_csv(r'homeprices.csv')
df

#EDA
#find out missing values in the dataset
df.isnull().sum()

import math
med=math.floor(df.bedrooms.median())
df.bedrooms=df.bedrooms.fillna(med)

import seaborn as sns
sns.lmplot(x='area',y='price',data=df)
sns.lmplot(x='bedrooms',y='price',data=df)
sns.lmplot(x='age',y='price',data=df)


from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(df[['area','bedrooms','age']], df.price)

reg.coef_ #m values-- array([   142.895644  , -48591.66405516,  -8529.30115951])
reg.intercept_ #b=


reg.predict([[3000,3,40]]) #array([427301.78627387])
reg.predict([[2500,4,5]])  #array([605787.84080221])
reg.predict([[3600,3,30]]) #a dataset from file--array([598332.18426826]) almost near to 595000


