
#Logisitic Regression
# SLR, MLR, PLR - to predict continuous values
# categorical value? 
'''
eg. 
email - spam/not spam
gender - male/female
marital status - single/married/widowed/divorced
party voting-congress/bjp/bjd
'''
# Binary classification using Logisitic Regression
# Dataset: insurance_data.csv
'''Introduce a new curve function: sigmoid/logit functon
sigmoid(t)=1/(1+e^-t), where t=Euler's no. = 2.71828.
Its max values can reach upto 1 only.'''

# Program-1
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"insurance_data.csv")
df

x=df.iloc[:,:-1].values #to be retrieved as 2D array
x
y=df.iloc[:,1].values #retrieve as 1D array
y

plt.xlabel('Age')
plt.ylabel('Have insurance?')
plt.scatter(x,y, marker='+',color='red')


#For the above data we cannot use linear regression
#show the data as logistic regression plot
import seaborn as sns
sns.regplot(x='age', y='bought_insurance',data=df, logistic=True, marker='+',color='red')


#create logistic regression model, train, find accuracy, make predictions
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x,y)
model.score(x,y) #0.8888888888888888
#predict if 56 years aged person will buy insurance ot not
model.predict([[56]]) #array([1], dtype=int64) - Yes
#predict if 36 years aged person will buy insurance or not
model.predict([[36]]) #array([0], dtype=int64) - No

