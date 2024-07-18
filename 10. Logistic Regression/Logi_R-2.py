
#Program-2
# dataset used: HR_comma_sep.csv (15000 rows, 10 cols)

import pandas as pd
df=pd.read_csv(r"HR_comma_sep.csv")
df.head()

#DATA EXPLORATION
#find no. of rows and cols sho left (i.e., left=1)
# and retained(i.e., left=0)
left=df[df.left==1]
left.shape #(3571, 10)
retained=df[df.left==0]
retained.shape #(11428, 10)

#find averages separately for left and retained people
#apply on numeric cols
numeric_cols = df.select_dtypes(include=[int, float]).columns
averages=df.groupby('left')[numeric_cols].mean()
averages
#since there is vast difference, the following are significant
# satisfaction-level, average_monthly_hours, Promotion_last_5_Years

#bar chart
# below bar graph shows that employees with high salary are not leaving (very less leaving)
pd.crosstab(df.salary, df.left).plot(kind='bar')
#bar chart showing relation b/w dept and left
df.dept.unique()
pd.crosstab(df.dept, df.left).plot(kind='bar')


#FROM ABOVE DATA ANALYSIS, we can conclude that:
'''we can use the following variables as dependent variables in our model:
    1. satisfaction-level, 2. Average monthly hours, 3. Promotion Last 5 years, 4. Salary'''
    
    
#--------------------------------------------------
subdf=df[['satisfaction_level', 'average_montly_hours', 'promotion_last_5years','salary']]
subdf.head()


#since salary is text, we will convert it into numbers.
#we should split salary variable into 'salary_high, salary_low, salary_medium.
#FOR THIS PURPOSE, we use dummy variables
salary_dummies=pd.get_dummies(subdf.salary, prefix='salary')
salary_dummies

#add the dummy variables to the data frame
df_with_dummies=pd.concat([subdf, salary_dummies], axis=1)
df_with_dummies.head()

#to avpid dummy varibale trap, let us delete salary_medium column
#we will also remove salary column as it is already represented by dummy variables

df_with_dummies.drop(['salary','salary_medium'],axis=1, inplace=True)
df_with_dummies.head()


# -------------------------------------------------------------

#take independent features (x) and target features(y)
x=df_with_dummies
y=df.left
#split the data into 70% train data and remaining 30% test data
from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test=train_test_split(x,y,train_size=0.7)

#apply Logistic Regression on the train data
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
#accuracy
model.score(x_test, y_test) #0.7773333333333333
model.score(x_train, y_train) # 0.7749309458043623
# ------------------------------------------------------------
#predictions

#find if employee will leave or stay back in the company when
#satisfaction level is 0.11, average monthly hours is 286, 
#No Promotion in last 5 years and medium salary=>(0,0)

inputs=[[0.11,286,0,0,0]]
model.predict(inputs)  #array([1], dtype=int64) => leaves the comapny


#find if employee will leave or stay back in the company when
#satisfaction level is 0.48, average monthly hours is 228, 
#No Promotion in last 5 years and low salary=>(0,1)

inputs=[[0.48,228,0,0,1]]
model.predict(inputs)   #array([0], dtype=int64) => stay in company


