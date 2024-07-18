
#Polynomial linear regression
# y=m1x1+m2x2^2+m3x3^3+...+mnxn^n+b 

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"Salary_Position.csv")
df

#retrive level col -1st column as 1D array
x=df.iloc[:,1:2].values
x
#retrive salary col -2nd column as 1D array
y=df.iloc[:,2].values
y

#scatter plot the dostribution of the data points
plt.scatter(x,y,color='red')
plt.show()

#create the SImple Linear Regression model
from sklearn.linear_model import LinearRegression
slr=LinearRegression()
slr.fit(x,y)
#predict the y vlaues based on x using the model
y_pred=slr.predict(x)
#now, plot the SLR line on the data points
plt.scatter(x,y,color='red')
plt.plot(x,y_pred,color='blue')
plt.show()



#Create ploynomial linear regreession model upto term let: x^2
from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=2)
#convert x into polynomial regrssion wuth degree 2
x1=pf.fit_transform(x)

#apply PLR on x1
plr=LinearRegression()
plr.fit(x1,y)
#predict y values based on x1
y_pred=plr.predict(x1)

#PLot the PLR - this fits the best
plt.scatter(x,y,color='red')
plt.plot(x, y_pred, color='blue')
plt.show()


#improving the polynomial linear regrssion model
#iincrease degree value from 1 to 8 and see the results again:
for i in range(1,9):
     pf=PolynomialFeatures(degree=i)
     x1=pf.fit_transform(x)
     plr.fit(x1,y)
     plt.scatter(x,y,color='red')
     plt.plot(x,plr.predict(x1), color='blue')
     plt.show()
     print('--------')
     

#From the output, deg values with 7 or 8 are fitting the given data points in best possible manner     
#let's use degree 7 for Polynomical Linear Regression model
pf=PolynomialFeatures(degree=7)
#convert x into polynomial regression with degree 7
x1=pf.fit_transform(x)
#apply PLR model on x1
plr=LinearRegression()
plr.fit(x1,y)

#observe the r2 value. Best fir if it is closet to 1
from sklearn.metrics import r2_score
r2_score(y, slr.predict(x)) #0.5537636591968075
r2_score(y, plr.predict(x1)) #0.9952325601657777

##OR
slr.score(x,y)  # 0.5537636591968075
plr.score(x1,y)   #0.9952325601657777


#Predict the salary for level 10 and 11 employees
inputs=[[10],[11]]
inputs1=pf.fit_transform(inputs)
plr.predict(inputs1)  #array([585184.15385371, 828604.60513514])