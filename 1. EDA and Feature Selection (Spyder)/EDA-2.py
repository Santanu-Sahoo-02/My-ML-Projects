
#working on titanic dataset
import pandas as pd
import seaborn as sns

df=pd.read_csv("titanic.csv")

print(df.shape)

df.info()

print(df.columns)

df.head()
df.tail()

#find the no. of missing values columnwise
#there are 177 in AGe col and 687 in Cabin col
df.isnull().sum()

#display the no. of rwos with missing values in the 'Age' col
df.Age.isnull().sum()

#display the rows of survived passengers
df[df.Survived==1]
len(df[df.Survived==1]) #gives 342
#display no. of people dead
len(df[df.Survived==0]) # gives 549

survived_df=df[df.Survived==1]
survived_df

dead_df=df[df.Survived==0]
dead_df

#display the names and ages of survived people
df[['Name','Age']][df.Survived==1]

#display  dataframe with only numeric datatypes
df1=df.select_dtypes(include=['float64','int64'])
df1

#draw distrbution plot on 'Age'
#highest no.of passengers around the age 20
sns.displot(data=df,x='Age',bins=10, kde=True, color='red')

#count the no.of people survived using countplot (show gender wise no.)
sns.countplot(data=survived_df, x= survived_df.Sex) #more females are saved

#count no, of people survived in Pclass
sns.countplot(data=survived_df, x= survived_df.Pclass) #more 1st class passengers have survived


