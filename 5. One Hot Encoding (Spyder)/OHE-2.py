

#A python program to understand how to encode categorical variables using One Hot Encdoing technique

#one hot encoding using sklearn OneHotEncoding
import pandas as pd

df=pd.read_csv(r"homeprices.csv")
df

#to use hot encoding, first we should use label encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
#fit and transform the data fram use le on town column
df.town=le.fit_transform(df.town)
df
#now, in new data: town will have 0,2 or 1
df

#retrieve training data
x=df[['town','area']]
x
#retieve target data
y=df.price
y

#apply One Hot Encoding on town columns
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(handle_unknown='ignore')

x1=ohe.fit_transform(df[['town']])
x1=pd.DataFrame(x1.toarray())
x1

#to avaoid dummy variab;e trap, drop 0th column
x1=x1.iloc[:,1:]
x1
#SO, 
                # 1   2
# monroe->       0.0,0.0; 
# west windsor-> 0.0,1.0; 
# robinsville->  1.0,0.0;


#add these columsn to x
x=pd.concat([x,x1], axis='columns')
x
#remove town as it is already encoded
x=x.drop('town', axis=1,inplace=True)
x

x.columns = x.columns.astype(str)  #If not used, THERE is a type error
# if you want feature names to be stored and validated, you must convert them all to strings, by using X.columns = X.columns.astype(str) for example. Otherwise you can remove feature / column names from your input data, or convert them all to a non-string data type.

#create linear regression model
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x, y)

#predict the price of house with 2800 sqft area, located at robinsville
model.predict([[2800,1,0]])  #array([590775.63964739])

#predict the price of house with 3400 sqft area, located at monroe township
model.predict([[3400,0,0]]) #array([641227.69296925]) 

#predict the price of house with 3400 sqft area, located at west windsor township
model.predict([[3400,0,1]]) #array([681241.6684584])

#Compared to OHE-1, here the order is different, because here 0th col is dropped; whereas in last example last col was dropped
#Accuracy
model.score(x,y)  #0.9573929037221873=> 95.7%