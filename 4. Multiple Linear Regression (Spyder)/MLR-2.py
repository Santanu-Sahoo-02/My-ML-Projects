

##Important
#Pprogram-2 on MLR

import pandas as pd
df=pd.read_excel(r"ca11-03homes.xls")

#STAGE-1
#EDA
df.isnull().sum()
#there are no missing values

#STAGE-2
#Outliers
#PLOTTING
import seaborn as sns
sns.lmplot(x='SqFt', y='Price',data=df)
sns.boxplot(x='BedRooms', y='Price',data=df)
sns.boxplot(x='Baths', y='Price',data=df)
#delete the rows with outliers using iqr method
q3=df.Price.quantile(.75)
q1=df.Price.quantile(.25)
iqr=q3-q1
ul=q3+(1.5*iqr)
ll=q1-(1.5*iqr)
#UPPER AND LOWER BOUND-Outliers
import numpy as np
upper=np.where(df.Price>=ul)
lower=np.where(df.Price<=ll)
upper
lower
#remove outliers
upper[0]
lower[0]
df.drop(upper[0],inplace=True) #gives the observation nos. from column-0
df.drop(lower[0],inplace=True)


#MLR
#retrieve 2nd, 3rd and 4th index-columns and take them as x
x=df.iloc[:,2:5]
x  #NOTE: it will give 479 rows and 3 columns, why? 26 outliers got removed-- 504-26=478
#retrieve 1st col as take it as y
y=df.iloc[:,1]
y

#take 80% data for training and 20% of data for testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2, random_state=10)

#train the comp with SLR model
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x_train, y_train)

y_pred=reg.predict(x_test)

#find the r squared value
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)  #y,y1 format - r2_score=0.829686049412441
# OR
reg.score(x_test,y_test) # 0.829686049412441
#82.96 % Accuracy

print(reg.predict([[780,3,1]])) #[56120.32684253]
print(reg.predict([[1500,3,2],[2000,4,4]]))  #[128866.13085266  205294.90136746]

