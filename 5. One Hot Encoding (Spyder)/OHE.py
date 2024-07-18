
import pandas as pd
df=pd.DataFrame()


#One Hot Encoding
#homeprices.csv- town as catogorical variable
#Converting texual data into Numeric Data


#APPROACH 1
#Label Encoding
'''
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df.town=le.fit_transform(df.town) #first sorts the values in alphabetical order and then replaces them by numeric values
#monroe township->0, robinsville->1, west windsor->2
'''
# Problem!
#the model thinks that 0<1<2
#So, monroe township<robinsville<west windsor -- which is wrong
'''hence, Label ENcoding is NOT recommended for catogorical data'''




#APPROACH 2
#use dummy variables - contain binary values 0 or 1

'''dummies=pd.get_dummies(df.town)''' #give the catogorical data inside
#sorts in alphabetical order and converts into binary digits
# monroe township->100; 1 for itself, robinsville->010, west windsor->001


#NOTE: in Linear Regression, independent variables don't depend on each other. - Hence, no reln exsit b/w them
#But, dummy variables are exactly opposite. 
#If we know any 2 values, we can predict the third value. Hence, they are nor completely independent
#Dummy variable trap- reln b/w independent variables and any two can predict the third


#To escape, the dummy variables trap, we should drop a value (drop the third value)
# monroe township->10;, robinsville->01, west windsor->00
'''dummies=dummies.drop('west windsor', axis=1)''' #1 represents columns




#APPROACH 3- One Hot Encoding- 2 stages
# stage-1: Label Encoding
# stage-2: convert these values into binary digits using OneHotEncoder class

#stage-1
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df.town=le.fit_transform(df.town) #first sorts the values in alphabetical order and then replaces them by numeric values
#town column values will contain 0,1 or 2
#monroe township->0, robinsville->1, west windsor->2

#stage-2
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(handle_unknown='ignore') #ignore categories that can't be converted
#Now, apply OHE on 'town'
x1=ohe.fit_transform(df[['town']]) #gives a sparse matrix
#convert it into array
x1=pd.DataFrame(x1.toarray())

# monroe township->(0th col known from stage-1)100; , robinsville->(1st col) 010, west windsor-> (2nd col) 001
#Now, conversions(encoding) is done.
#Drop a column
x1=x1.iloc[:,1:] #drop 0th col



