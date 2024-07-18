# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:35:30 2024

@author: Santanu Sahoo
"""
##TOPIC: --distribution plot - displot
# import matplotlib.pyplot as plt
# import seaborn as sns
# mpg=sns.load_dataset('mpg') #import the dataset from Internet--- returns pandas dataset to mpg on left

# ##to show only histogramkip kde
# # sns.displot(data=mpg,x='cylinders',bins=5,kde=True) #kernel density estimate=True, #bins=5-->5 intervals

# ##without histogram, showing only kde:
# # sns.displot(data=mpg,x='cylinders',kind='kde')

# ##DISPLAY emperical cumulative ditribution function-- fro proportional densities
# # sns.displot(data=mpg,x='cylinders',kind="ecdf")

# ##distribution plot with cylinders on x and miles per gallon(mpg) on y
# sns.displot(data=mpg,x='cylinders',y='mpg')

# ##kde of above graph
# sns.displot(data=mpg,x='cylinders',y='mpg',kind='kde')
# plt.xlabel("No.of Cylinders")
# plt.ylabel("Mileage")

# plt.show()


# # TOPIC: --count plot - countplot
# import matplotlib.pyplot as plt
# import seaborn as sns
# mpg=sns.load_dataset('mpg') 

# #showing count plot where no.of cylinders are grouped and counted
# ##no.of cylinders on x, count no. of records on y
# # sns.countplot(x='cylinders',data=mpg)

# #to see countrywise no.of cars
# mpg.origin.unique()  #this display: array(['usa', 'japan', 'europe'], dtype=object)
# sns.countplot(x='cylinders',data=mpg,hue='origin') #at left - color boc with country- LEGEND
'''
In Seaborn's countplot, "hue" does not stand for a full form. 
It's a parameter that allows you to add another dimension to your plot 
by coloring the bars based on a categorical variable.
'''
# # plt.legend(loc='upper right')
# plt.xlabel("no.of cylinders")
# plt.ylabel('no.of cars')

# plt.show()





# TOPIC: --BOX Plot--sns.boxplot()
# import matplotlib.pyplot as plt
# import seaborn as sns
# mpg=sns.load_dataset('mpg') 

# sns.boxplot(data=mpg, x='origin',y='acceleration') #at left - color boc with country- LEGEND

# plt.show()



# #TOPIC: --Scatter Plot
# import matplotlib.pyplot as plt
# import seaborn as sns
# mpg=sns.load_dataset('mpg') 

# # sns.scatterplot(data=mpg, x='horsepower',y='acceleration') 
# #to know which point is correspinding to which country's origin
# sns.scatterplot(data=mpg, x='horsepower',y='acceleration',hue='origin') 

# plt.show()




# #TOPIC: --Joint Plot-- jointplot()----SCATTERPLOT+HISTOGRAM
# import matplotlib.pyplot as plt
# import seaborn as sns
# mpg=sns.load_dataset('mpg') 
# sns.jointplot(data=mpg, x='horsepower',y='acceleration') 
# # ##sns.jointplot(data=mpg, x='horsepower',y='acceleration',hue='origin') 

# plt.show()




# #TOPIC: --Line Plot-- lineplot()
# import matplotlib.pyplot as plt
# import seaborn as sns
# mpg=sns.load_dataset('mpg') 
# ##sns.lineplot(data=mpg, x='horsepower',y='acceleration') 
# sns.lineplot(data=mpg, x='horsepower',y='acceleration',hue='origin') 

# plt.show()



# #TOPIC: -SCATTER+REGRESSION LINE -- lmplot()
# import matplotlib.pyplot as plt
# import seaborn as sns
# mpg=sns.load_dataset('mpg')  
# sns.lmplot(data=mpg, x='horsepower',y='acceleration') 

# plt.show()





# #TOPIC: -Regression plot-- regplot()---giving same output as above program
# import matplotlib.pyplot as plt
# import seaborn as sns
# mpg=sns.load_dataset('mpg')  
# sns.regplot(data=mpg, x='horsepower',y='acceleration') 

# plt.show()


#creating subplots



#display 3 different plots as sub plots in a grid of 2 rows and 2 columns
#TOPIC: -Regression plot-- regplot()---giving same output as above program
import matplotlib.pyplot as plt
import seaborn as sns
mpg=sns.load_dataset('mpg')  

#crrate subplots in a space of 10x10 inches
plt.figure(figsize=(10,10))
#
plt.subplot(2,2,1)
sns.scatterplot(data=mpg, x='horsepower',y='acceleration',hue='origin') 
#
plt.subplot(2,2,2)
sns.scatterplot(data=mpg, x='horsepower',y='acceleration') 
#
plt.subplot(2,2,3)
sns.boxplot(data=mpg, x='origin',y='acceleration',hue='origin') 




plt.show()
