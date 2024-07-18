

#EDA
#Datadet-CARS.csv-downloaded from kaggle
import pandas as pd
import seaborn as sns
cars=pd.read_csv("CARS.csv")

#show how many rows and cols
print(cars.shape)

#dataset info
cars.info()

# display top 5 rows
cars.head()
# display top 10 rows
cars.head(10)
# display last 5 rows
cars.tail()

# remove unimportant cols: MSRP, INVOICE
cars=cars.drop(['MSRP','Invoice'],axis=1)

#remove duplicate rows if any
#keep first row and remove other duplicate rows of that row
cars=cars.drop_duplicates(keep='first')

#to find the total no. of rows which are missing value in a column
cars.isnull().sum()

#remove the rows having missing values (in cylinders)
cars.dropna(inplace=True)

# @sort the data w.r.t a column -- let's sort 'MPG_City' in desc order
cars_sort=cars.sort_values(by='MPG_City', ascending=False)

#iloc-> gives int location based on indexing/selection
cars.iloc[[0,2,4],[1,3,5]]

#select first 5 rows in mpg_city col using ""iloc"" and ""loc""
x=cars.iloc[0:5,8]
x
x=cars.loc[0:5,'MPG_City']
x


#TO select only numeric type of columns, we can give their (1) names or (2) datatypes
cars1=cars[['EngineSize','Cylinders','Horsepower','MPG_City','MPG_Highway', 'Weight', 'Wheelbase', 'Length']]
cars1
cars1=cars.select_dtypes(include=['float64','int64'])
cars1


#summart statistics
#if std is 0, that solumn should be removed from analysis
cars.describe()

#find co-relations between all columns
cars.corr(numeric_only=True)   #replaced --method='pearson' ---by---numeric_only=True

#find correltions between all coumns and 'MPG_City'
cars.corr(numeric_only=True)['MPG_City']

#display a distribution plot with kernel density estimate
#estimate lime. Takr MPG_City on x axis
sns.displot(data=cars,x='MPG_City',bins=10,kde=True, color='blue')

#draw regression plot between length og th car and mileage in city
sns.regplot(x='Length',y='MPG_City',data=cars)

#box plot can be drawn only for catogorical variables
#SUV gives less mileage and Hybrid gives more mileage
box1=sns.boxplot(data=cars,x='Type', y='MPG_City')

#THe origin of car in ASIA gives slightly more mileage
box2=sns.boxplot(data=cars,x='Origin', y='MPG_City')


#drae okar plots between columns
sns.pairplot(cars, hue='Origin')
