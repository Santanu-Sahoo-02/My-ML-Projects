

#Polynomial linear regression
# y=m1x1+m2x2^2+m3x3^3+...+mnxn^n+b 

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"Salary_Experience.csv")
df

#retrive 0th col as x
x=df.iloc[:,0:1].values
x
#retrive 1st column as y
y=df.iloc[:,1].values
y

#scatter plot the distribution of the data points
plt.scatter(df['YearsExperience'], df["Salary"])
plt.scatter(x,y)
plt.xlabel("Years of Experince")
plt.ylabel("Salary")
plt.title("Salary V/s Years of Experience")
plt.show()

#Create ploynomial linear regreession model upto term let: x^5
from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=5)
#convert x into polynomial regrssion wuth degree 5
x1=pf.fit_transform(x)

#create PLR model and apply PLR on x1
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x1,y)

#observe the r2 value. Best fir if it is closet to 1
from sklearn.metrics import r2_score
r2_score(y, lr.predict(x1)) 
##OR
lr.score(x1,y)    #0.9654464875724768

#Plot the PLR - this fits the best
plt.scatter(x,y,color='red')
plt.plot(x, lr.predict(x1), color='blue')
plt.show()


#find the coefficient
#since deg is 5, we will have 5 coefficients
print("Coefficients:", lr.coef_)
# Coefficients: [ 0.00000000e+00  4.97578180e+04 -2.29457152e+04  5.29768731e+03
#  -5.24237382e+02  1.85349746e+01]

#find intercept
print("Intercept: ",lr.intercept_) #4792.361311448403

#Judge the salary of employee with 5.5 yrs of experience
#NOTEL input should be in 2D and output will be in 1D array form
inputs=[[5.5]]
inputs1=pf.fit_transform(inputs)
result=lr.predict(inputs1)
print("Salary for 5.5 yrs experince=", result)