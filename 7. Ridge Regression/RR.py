
#Ridge Regression

#Concept of bias anf variance - inverse relationship
# We need - low bias, low variance - correct model, correct predictions

#Unfitting - High bias; low variance
# Overfitting - Low Bias; High variance
'''
An overfitted model generates very high accuracy scores during the training phase. 
An underfitted model performs poorly, even with the training data.

'''
# Concept of Regularisation - Ridge R, Lasso R, ElasticNet R - to minimise variance


'''
SIMPLE LINEAR REGRESSION:
    equation of line + (sum of squared residuals) => Deviation
    
Regularisation parmater - LAMBDA
When LAMBDA is increased, it reduces variance. but if increased too much, then HIGH bias,

Penanlty term/parameter: LAMBDA x square of slope  => Also called, L2 Penanlty Term

RIDGE REGRESSION:
    equation of line + sum of quared residuals + (LAMBDA * square of slope)
    if LAMBDA=0 => SLR:
        
0<LAMBDA<infinity

'''

#Ridge regression to predict height depending on weight
#Fit SLR on traning data and RR in testing data
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge

#load train data into x and test data into y
x=pd.read_csv(r"train.csv")
x
y=pd.read_csv(r"test.csv")
y
#take the data into x and y variables
w_train=x.iloc[:,0:1].values
h_train=x.iloc[:,1].values
w_test=y.iloc[:,0:1].values
h_test=y.iloc[:,1].values

#draw scatter plot for train and test data in the same graph
plt.scatter(w_train,h_train, color='blue', marker='o')
plt.scatter(w_test, h_test, color='red', marker='d')
plt.show()



#using SLR:
lr=LinearRegression()
lr.fit(w_train, h_train)
#score
lr.score(w_train,h_train)  #0.9554154968329801
#draw scatter and plot with original data and predicted line
plt.scatter(w_train,h_train, color='blue')
plt.plot(w_train, lr.predict(w_train), color='orange')
plt.show()



#using RR:
rr=Ridge(alpha=.001)
rr.fit(w_test, h_test)
#score
rr.score(w_test, h_test) # 0.8901155976774442
#draw scatter and plot with original dataand redicted line
plt.scatter(w_test,h_test, color='red')
plt.plot(w_test, rr.predict(w_test), color='green')
plt.show()


#predict height og a perspn having wt=70.3 kg
rr.predict([[70.3]]) # array([6.27334337]) =?6.27 feet

