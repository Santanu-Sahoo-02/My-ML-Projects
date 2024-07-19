
#LR-2

import pandas as pd
df=pd.read_csv(r"Advertising.csv")
df.head()

#see the names of columns
names=df.columns
names

#to delete the unnamed column, first rename it as 'a' column, then drop it
df.rename({"Unnamed: 0":"a"}, axis='columns', inplace=True)
df.drop(["a"], axis=1,inplace=True)
    
#drop sales and take rest as x
x=df.drop('sales', axis=1)
x
#take MEDV as y
y=df.sales.values
y

#take the names of 0,1,2nd col
names=x.columns
names
#Range of columns - this gives 0 to 3
rng=range(len(names))
rng



#APPLY LR on the data
#after the model is trained, find the coefficients
from sklearn.linear_model import Lasso
ls=Lasso(alpha=0.1)
model=ls.fit(x,y)
cf=model.coef_
cf  #array([ 0.04575172,  0.18788735, -0.00066758])

#draw the plot b/w col no. and coeff
import matplotlib.pyplot as plt
plt.plot(rng, cf)
plt.xticks(rng, names, rotation=60)
plt.ylabel("Coefficients")
plt.show()

#find accuracy
ls.score(x, y) #0.8972068586756202

'''find the sales is compant is spending dollars :
    150 on TV, 41 on radio, 60 on newspaper'''
newdata=[[150,41,60]]
sales=model.predict(newdata)
sales #array([17.47052333])
#OR
# sales=ls.predict(newdata)
# sales #array([17.47052333])
