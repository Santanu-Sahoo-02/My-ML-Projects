# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:06:15 2024

@author: Santanu Sahoo
"""

#histogram
#display histogram showing the no. of employees in a specific age group
import matplotlib.pyplot as plt

emp_ages=[22,45,30,59,58,56,57,45,43,43,50,40,34,33,25,19]
bins=[0,10,20,30,40,50,60]

plt.hist(emp_ages,bins,histtype='bar',rwidth=0.8,color='blue')

plt.xlabel("Employee ages")
plt.ylabel('no.of.employees')

plt.title("ORACLE CORP")
plt.legend()

plt.show()