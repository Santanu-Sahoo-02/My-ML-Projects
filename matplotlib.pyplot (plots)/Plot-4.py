# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:13:13 2024

@author: Santanu Sahoo
"""

#pie-chart
#display employees of different depts in pie chart

import matplotlib.pyplot as plt

slices=[50,14,24,16] #expenditure of 4 departments
depts=['sales','production','HR','Finance']
cols=['magenta','cyan','brown','gold']

plt.pie(slices,labels=depts,colors=cols,startangle=90, explode=(0,.2,0,0), shadow=True, autopct="%.2f%%")

plt.title('WIPRO-Departmentwise Expenditure')
plt.legend()

plt.show()
