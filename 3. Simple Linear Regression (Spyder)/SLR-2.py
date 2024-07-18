
#Program 2
#Train the comp. using SLR model on the employee experience and salary data.
#Predict the salary of an employee having 11 years of experience

import pandas as pd
import matplotlib.pyplot as plt
#PART1
dataset=pd.read_csv("Salary_Data.csv")
#retrieve on;y 0th column and take it as x--- [0:last]==> 0th col since 2 cols
x=dataset.iloc[:,:-1].values
x
#retrieve only the 1st col and take it as y
y=dataset.iloc[:,1].values
y

plt.scatter(x,y)


#PART2
#take 70% of data for training and 30% for testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=0)

#train the comp. with SLR mdoel
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x_train, y_train)

#test the model by passing test data and obtain predicted data]
#test data is:
x_test
y_pred=reg.predict(x_test) #x_test is taken randomly form file (30%) and y_pred is done based on trained model (of 70% data)
y_pred  #Y1



#PART3
##find accuracy level of the model by finding r squared values
from sklearn.metrics import r2_score #sklearn-package; metrics-module; r2_score-function
r2_score(y_test, y_pred)  #(y,y1)--(original,predicted)- of 30% data
#0.9740993407213511==> 97.4% accuracy


# PART4 --- predict for new data -- for 11 years of experience
print(reg.predict([[11]]))  #[129740.26548933]




#""PART5""
#using matplotlib, draw catter and line plot on x_train
plt.scatter(x_train, y_train, color='red')   ##using actual vlaues
plt.plot(x_train, reg.predict(x_train),color='blue') ## using predicted values
plt.tile("Experience vs Salary")
plt.xlabel("Yrs of exp")
plt('salary')

plt.show()


