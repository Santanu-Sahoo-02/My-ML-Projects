
#Display emp id on x axis and their salaries on y-axis in form of bar graph for two dpeartments of a company

import matplotlib.pyplot as plt

#data
#Sales dept
x=[1001,1003,1006,1007,1009,1011]
y=[10000,23000.5,18000.33,16500.50,12000.75,9999.99]
#Production dept
x1=[1002,1004,1010,1008,1014,1015]
y1=[5000,6000,4500.00,12000,9000,10000]
#create bar graphs
plt.bar(x,y,label="Sales dept", color="red")
plt.bar(x1,y1,label="Production dept", color="blue")
#set labels and legends
plt.xlabel("Employee ids")
plt.ylabel("Employee salaries")

plt.title("MICROSOFT INC")
plt.legend()#show legend

plt.show() #display graph

