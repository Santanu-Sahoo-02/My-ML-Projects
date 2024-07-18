
#Program 3
#find out per capita income of canada during years 2020,2021 based on per capita income data provided
#use SLR model

import pandas as pd
import matplotlib.pyplot as plt

#PART1
dataset=pd.read_excel("canada_per_capita_income.xlsx")
#retrieve on;y 0th column and take it as x
x=dataset.iloc[:,0:1].values
x
#retrieve only the last (or 1st) col and take it as y
y=dataset.iloc[:,-1].values
y

plt.scatter(x,y,color='red')


#PART2
#take 70% of data for training and 30% for testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=5)

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

#Method-1
r2_score(y_test, y_pred)  #(y,y1)--(original,predicted)-of 30% data
#0.8433026110551844
#Method-2
reg.score(x_test,y_test)  #(x_test, y_test)
#0.8433026110551844
#So, 84.3% accuracy


# PART4 --- predict for new data -- 
print(reg.predict([[2020],[2021]]))  #[41819.49650873 42681.02869595]




#""PART5""
#using matplotlib, draw catter and regression line  on x_train
plt.scatter(x_train, y_train, color='red')   ##using actual values
plt.plot(x_train, reg.predict(x_train),color='blue') ## using predicted values
plt.tile("PER CAPITA INCOME OF CANADA")
plt.xlabel("Year")
plt('Per Capita Income')

plt.show()

