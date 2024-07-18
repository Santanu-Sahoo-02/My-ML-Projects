

#Linear Regression Model (Lease Sqaures RM)
# from sklearn.metrics import r2_score #sklearn-package; metrics-module; r2_score-function
# y=[1,2,3,4,5]
# y1=[.8,2.5,3,4.8,4.4]
# R_Square=r2_score(y,y1)
# print("Co-efficient of Determination:", R_Square)

#program
#predict the price of a house in New Yor depending on its area.
#Given: the house area, find ou the prices of the houses whose area areL 3300 sqft and 5000 sqft
#price=m*area+b+E

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

df=pd.read_csv("homeprices.csv")
df

sns.scatterplot(data=df, x='area', y='price')

'''once we see the scatter plot, we can understand that the
distribution is linear and can use Linear Reg Model'''

reg=LinearRegression()
reg.fit(df[['area']], df.price) #fitting means training 
#in above df.price is the output which is returned
#here, in reg.fit(x,y), x=df.area supplied in 2d matrix form
# way 1: df.area.values.reshape(-1,1)
# way 2: df[['area']]

#predict the price of 3300 sqft house
reg.predict([[3300]]) #gives 628715.75342466 -- y=mx+b+E


##CHECK! FIND m and b
#find the coefficient - this ths slope m
reg.coef_ #135.78767123
#find the intercept b
reg.intercept_ #180616.43835616432
#if we substitute m and b in y=mx+b
y=135.78767123*3300 + 180616.43835616432
y #gives 628715.7534151643



#next predict the price of 5000 sqft house
reg.predict([[5000]]) #gives 859554.79452055

##find accuracy level of the model by finding r squared values
from sklearn.metrics import r2_score #sklearn-package; metrics-module; r2_score-function
y=df.price
y1=reg.predict(df[['area']])
R_Square=r2_score(y,y1)
print("Co-efficient of Determination:", R_Square)
#95.8% accuracy

sns.lmplot(data=df,x='area',y='price')



#n this example all rows are used to train
#Genrally, 70% of rows are used to train and the remaining 30% rows are used for testing purpose
