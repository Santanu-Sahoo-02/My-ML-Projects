
#Divide the data into training and test data. Fit SLR on traning data and RR in testing data
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge

#load train data into x and test data into y
df=pd.read_csv(r"boston_houses.csv")
df
#take the RM( 5th col) as x and convert into 2D array
x=df.iloc[:,5:6].values
x
#take the Price (last col) as y and convert into 1D array
y=df.iloc[:,-1].values
y
#split the data into train and test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.2, random_state=1)

#draw scatter plot for train and test data in the same graph
plt.scatter(x_train,y_train, color='blue', marker='^')
plt.scatter(x_test, y_test, color='red', marker='+')
plt.show()



#using SLR:
lr=LinearRegression()
lr.fit(x_train,y_train)
#score
lr.score(x_train,y_train)  

#draw scatter and plot with original data and predicted line
plt.scatter(x_train,y_train, color='blue',marker='^')
plt.plot(x_train, lr.predict(x_train), color='red')
plt.show()



#using RR:#take alpha values as 0.001, 0.01, 0.05, 0.5, 1,2, etc.
rr=Ridge(alpha=0.01)
rr.fit(x_test, y_test)
#score
rr.score(x_test, y_test) # 0.6055889226873513
#draw scatter and plot with original dataand redicted line
plt.scatter(x_test,y_test, color='red', marker='+')
plt.plot(x_test, rr.predict(x_test), color='green')
plt.show()


#predict price of a house having 6.5 rooms
rr.predict([[6.5]]) #array([24.14866523])
