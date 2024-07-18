# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:26:29 2024

@author: Santanu Sahoo
"""

#scatter graph
#to display relationship between ages and prices of houses at Delhi

import matplotlib.pyplot as plt
# import numpy as np
age=[6,8,9,2,10,2,9,4,11,12,9]
price=[97,87,82,120,77,122,99,97,74,79,83] #can use 1D array-np.array(List)

plt.scatter(age,price,color='red',marker='d')

plt.xlabel('Age in yers')
plt.ylabel('Price in Lakhs of Rs')

plt.title('Ages and Prices at Delhi')
plt.legend()

plt.show()

