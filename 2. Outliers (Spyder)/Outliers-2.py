

#Outliner detection and handling
#write a program to substitute mean value in the place of outliers in the
#'Ash, Sand & Dust used in Asphalt Production' column in Solid Waste Generation dataset
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("Solid_Waste_Generation___Recycling.csv")
data.shape #gives (15,80)
#rename(shorten) the column
data.rename(columns={'Ash, Sand & Dust used in Asphalt Production':'target'},inplace=True)


df=data.sort_values('target')
#display all rows of target column (this is 5th column). [NOTE: 0s cannot be outliers]
#but last row has 40409 - this is outlier
df.iloc[:,5]


#Way-2 Plotting
sns.boxplot(data=data,x='target')
sns.displot(data=data, x='target',bins=20)

#Way-3 IQR method
q3=data['target'].quantile(.75)
q3 #gives11454.5
q1=data['target'].quantile(.25)
q1 #gives 0.0
iqr=q3-q1
iqr #11454.5

#cal. upper and lower limits from iqr
ul=q3+(1.5*iqr)
ll=q3-(1.5*iqr)
print(ll,ul) #gives -5727.25 28636.25

upper=np.where(data['target']>=ul)
upper
lower=np.where(data['target']<=ll)
lower

upper[0]
lower[0]
# '''#SOL-1'''
#delete the rows above upper and below lower values
data.drop(upper[0], inplace=True)
data.drop(lower[0], inplace=True)

data.shape #gives(14,80)

data #row with index 4 is removed


'''#SOL-2 (using df1)'''
#let's replace the outliers with a value
#convert the Aluminum Cans into an array
df1=pd.read_csv("C:\\Users\\Santanu Sahoo\\Desktop\\ML Datasets\\18. Outliers\\Solid_Waste_Generation___Recycling.csv")
df1.rename(columns={'Ash, Sand & Dust used in Asphalt Production':'target'},inplace=True)
arr=df1['target'].values
# if arr values are between ll and ul, represent that value as True, else False
#False values are outliers

true_index=(ll<arr) & (arr<ul)
true_index

#caluclate the mean of all other values (except the outliers)
mid=np.mean(df1['target'][true_index]) #mean of all true_index values
mid #returns 5358.857142857143

#replace all outliers with mean value
false_index=~true_index
false_index
df1['target'].values[false_index]=mid #replaces 40409 by 5358
df1['target']
