

# #ElasticNET Regression Model --> COmbination of RR and LR
# It is used when large no. of columns are there with large volume of data.
# Penanlty term: equation of line + (sum of sqaured residuals) + (LAMBDA1) * |slope| + (LAMBD2) * (slope)^2
# When LAMBDA1 =0 => RR and When LAMBDA2=0 => LR
#Whenn penanlties are greater than 0, it is ElasticNET Regression

#NOTE: LR undestands which colujmn is influencing the output more, but it will not use that column alone.
#It is more accurate that LR.


import pandas as pd
boston=pd.read_csv(r"boston_houses.csv")
boston.head()


#drop MEDV and take rest as x
x=boston.drop('MEDV', axis=1)
x
#take MEDV as y
y=boston.MEDV.values
y
#take the names of 0 to 13th columns
names=x.columns
names
#Range of columns - this gives range(0, 13)
rng=range(len(names))
rng



#APPLY ElasticNET R.model on the data
#create an object to ElasticNet class
from sklearn.linear_model import ElasticNet
es=ElasticNet(l1_ratio=0.5)
#train the model
model=es.fit(x,y)
#find the coeff
es_cf=model.coef_
es_cf
'''array([-0.08037077,  0.05323951, -0.0126571 ,  0.        , -0.        ,
        0.93393555,  0.0205792 , -0.76204391,  0.30156906, -0.01643916,
       -0.7480458 ,  0.00833878, -0.75842612])'''
#find the position of max value in the coeff
import numpy as np
n=np.argmax(es_cf)
n #gives 5 - 6th column
#find the col name at nth position in x.
print("The most influencing column = ", names[n])


#draw the plot b/w col no. and coeff
import matplotlib.pyplot as plt
plt.plot(rng, es_cf)
plt.xticks(rng, names, rotation=60)
plt.ylabel("Coefficients")
plt.show()
