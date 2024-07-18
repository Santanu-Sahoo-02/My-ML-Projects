# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:21:17 2024

@author: Santanu Sahoo
"""
#display profits of a company in different years using line graph

import matplotlib.pyplot as plt

years=['2015','2016','2017','2018','2019','2020','2021'] #expenditure of 4 departments
profits=[9,10,10.5,8.9,12.75,7.51,6.45]


plt.plot(years,profits,'blue')
plt.xlabel('Years')
plt.ylabel('Profits in Million Rs')

plt.title('XYZ Company')
plt.legend()

plt.show()
