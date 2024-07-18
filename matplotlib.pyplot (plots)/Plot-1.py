# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:34:52 2024

@author: Santanu Sahoo
"""


#matplotlib.pyplot
#data visualisation

#Display emp id on x axis and their salaries on y-axis in form of bar graph
import matplotlib.pyplot as plt
import pandas as pd


empdata={"empid":[1001,1002,1003,1004,1005,1006],\
         "ename":["Ganesh Rao","Anil Kumar","Gaurav Gupta","Hema CHandra","Laxmi Prasanna","Anant Nag"],\
        "sal":[10000,23000.5,18000.33,16500.5,12000.75,9999.99],\
        "doj":["10-10-2000","3-20-2002","3-3-2002","9-10-2000","10-8-2000",'9-9-1999']}
df=pd.DataFrame(empdata)

x=df['empid']
y=df['sal']
#PLOT
plt.bar(x,y,label="Employee data", color="red")
plt.xlabel("Employee ids")
plt.ylabel("Employee salaries")
plt.title("MICROSOFT INC")
plt.legend()#show legend
plt.show() #display graph

