

#LR
#penanlty term: LAMBDA x modulus of slope =>L1 penanlty term
'''
Lasso Regression:
    Equation of line + sum of quared residuals + LAMBDA x |slope|
LR offers some bias and very low variance.

NOTE:
    1. LR is used to reduce variance and is more accurate than RR.
    2. RR- considers all columns. LR-selects only 1 col, that has max influence on final result.
'''

#Feature Selection (feature/column)
#About dataset boston_houses.csv:
'''Crime rate, no. og rooms in house, age of house, whether loacted at riverside, property tax, 
how many blacks are living there, etc'''
'''Price is represented by last col MEDV-Median Value (of the house)'''
# let's consider, if age is high, price may be low. SO, how to select the columns?
# Answer: LR model. - internall uses an algo to understand which feature is most imp.
# LR:
#     y=m1x1+m2x2+m3x3+...+b+ (sum of squared residuals) + (LAMBDA x |slope|)
    

import pandas as pd
boston=pd.read_csv(r"boston_houses.csv")
boston.head()

#see the names of columns
names=boston.columns
names

#to delete the unnamed column, first rename it as 'a' column, then drop it
boston.rename({"Unnamed: 0":"a"}, axis='columns', inplace=True)
boston.drop(["a"], axis=1,inplace=True)
    
#drop MEDV and take rest as x
x=boston.drop('MEDV', axis=1)
x
#take MEDV as y
y=boston.MEDV.values
y

#take the names of 0 to 13th columns
names=x.columns
names
#Range of columns - this gives 0 to 13
rng=range(len(names))
rng



#APPLY LR on the data
#after the model is trained, find the coefficients
from sklearn.linear_model import Lasso
ls=Lasso(alpha=0.1)
data=ls.fit(x,y)
cf=data.coef_
cf

#draw the plot b/w col no. and coeff
import matplotlib.pyplot as plt
plt.plot(rng, cf)
plt.xticks(rng, names, rotation=60)
plt.ylabel("Coefficients")
plt.show()

#find accuracy
data.score(x, y) #0.7269834862602695

'''find the price (MEDV) of house when:
    CRIM=0.02731, ZN=0, INDUS=7.07, CHAS=0, NOX=0.469, RM=6.421,
    AGE=78.9, DIS=4.6971, RAD=2, TAX=242, PTRATIO=17.8, BLACK=396.9,
    LSTAT=9.14'''
newdata=[[0.02731,0,7.07,0,0.469,6.421,78.9,4.6971,2,242,17.8,369.9,9.14]]
price=data.predict(newdata) #array([24.74908573])
price
#OR
# price=ls.predict(newdata)
# price
