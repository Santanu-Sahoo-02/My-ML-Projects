# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:22:13 2024

@author: Santanu Sahoo
"""

# ##Iris dataset

# #TOPIC- HeatMap - heatmap()
# #-colour encoded matrix
# import matplotlib.pyplot as plt
# import seaborn as sns
# iris=sns.load_dataset('iris')  

# # #take first 10 rows and first 4 columns
# iris1=iris.iloc[0:10,0:4]
# #annot-writes the values in the cell, cmap (colour of map) attribute
# sns.heatmap(iris1,cmap='RdBu',annot=True)
# #cmap--'coolwarm','BrBG','RdBu','Blues'

# plt.show()


# #TOPIC- catplot()
# #this can be useful to complaare the sepal lemgth of all 3 types represntes by species column
# import matplotlib.pyplot as plt
# import seaborn as sns
# iris=sns.load_dataset('iris')  


# sns.catplot(data=iris, x='species',y='sepal_length')
# #from plot- virginica flowers have more sepal length
# plt.show()



# # Subtopic- VIOLIN PLOT using kind
# #variation of catplot() where data is displayed in form of violin
# import matplotlib.pyplot as plt
# import seaborn as sns
# iris=sns.load_dataset('iris')  

# sns.catplot(data=iris, x='species',y='sepal_length',kind='violin')
# #from plot- virginica flowers have more sepal length
# plt.show()


# # Subtopic- BOX PLOT using kind
# #variation of catplot() where data is displayed in form of box
# import matplotlib.pyplot as plt
# import seaborn as sns
# iris=sns.load_dataset('iris')  

# sns.catplot(data=iris, x='species',y='sepal_length',kind='boxen')
# #from plot- virginica flowers have more sepal length
# plt.show()



# Topic- pairplot()
#it shows relationship of every column with all other columns (numeric columns)
import matplotlib.pyplot as plt
import seaborn as sns
iris=sns.load_dataset('iris')  

# sns.pairplot(data=iris,hue='species') #hue is used for diffrent colors for diff. flowers

##picking colors--palette='cubeheelix'/'husl'/'coolwarm'...
# sns.pairplot(data=iris,hue='species',palette='cubehelix')

##also, we can change shape of pointers. circle-'o',diamond-'d',square-'s'
sns.pairplot(data=iris,hue='species',palette='coolwarm',markers=['o','d','s'])


plt.show()