

#Outliers
'''
3 ways to detect:
    - sorting the data
    - drawing graphs/plots
    -  IQR method
'''


#Outliner detection and handling
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("Solid_Waste_Generation___Recycling.csv")

#keep original data into df1 for later use
df1=data
data.shape #gives (15,80)

#Way-1 sorting
df=data.sort_values('Aluminum Cans')
df['Aluminum Cans'].head()
df['Aluminum Cans'].tail()

#Way-2 Plotting
sns.boxplot(data=data,x='Aluminum Cans')
plt.show()
sns.displot(data=data, x='Aluminum Cans',bins=10)

#Way-3 IQR method
q3=data['Aluminum Cans'].quantile(.75)
q3
q1=data['Aluminum Cans'].quantile(.25)
q1
iqr=q3-q1
iqr

#cal. upper and lower limits from iqr
ul=q3+(1.5*iqr)
ll=q3-(1.5*iqr)
print(ll,ul) #11890.25 20798.75


upper=np.where(data['Aluminum Cans']>=ul)
upper
lower=np.where(data['Aluminum Cans']<=ll)
lower

upper[0]
lower[0]
# '''#SOL-1'''
# #delete the rows above upper and below lower values
# data.drop(upper[0], inplace=True)
# data.drop(lower[0], inplace=True)

# data.shape #gives(14,80)

# data #row with index 9 is removed


'''#SOL-2 (using df1)'''
#let's replace the outliers with a value
#convert the Aluminum Cans into an array
df1=pd.read_csv("C:\\Users\\Santanu Sahoo\\Desktop\\ML Datasets\\18. Outliers\\Solid_Waste_Generation___Recycling.csv")
arr=df1['Aluminum Cans'].values
# if arr values are between ll and ul, represent that value as True, else False
#False values are outliers

true_index=(ll<arr) & (arr<ul)
true_index

#caluclate the median of all other values (except the outliers)
mid=np.median(df1['Aluminum Cans'][true_index]) #median of all true_index values
mid #returns 14157.0

#replace all outliers with median value
false_index=~true_index
false_index
df1['Aluminum Cans'].values[false_index]=mid
df1['Aluminum Cans']


