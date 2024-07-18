
#A python program to understand gow to encode categorical variables using dummy variables

import pandas as pd
df=pd.read_csv(r"homeprices.csv")
df

dummies = pd.get_dummies(df.town)
dummies

#to avaoid dummy variable trap, remove 'west windsor'
dummies=dummies.drop(['west windsor'], axis='columns')
dummies

#add these to original df
merged=pd.concat([df,dummies], axis='columns')
merged

#we don't require 'town' variable as it is replaced by dummy variables
final=merged.drop(['town'],axis='columns')
final

#we have to delete the price columns as it is the target columns
#to be predicted
x=final.drop(['price'], axis='columns')
x

y=final['price']
y


#Even though we do not drop the dummy variable,
#linear regression model will work correctly
#the reason isL it will internallt drop a column


#Create LR model:
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)

#predict the price of house with 2800 sqft area, located at robinsville
#parameter: 1st: are, 2nd: monroe township, 3rd: robinsville
model.predict([[2800,0,1]])  #array([590775.63964739])

#predict the price of house with 3400 sqft area, located at west windsor
model.predict([[3400,0,0]]) #array([681241.66845839])

#Accuracy
model.score(x,y)  #0.9573929037221873=> 95.7%