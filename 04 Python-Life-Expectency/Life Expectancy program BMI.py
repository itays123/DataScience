# Write your code here :-)

import numpy as np
import matplotlib.pyplot as plt

# Grid Settings
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.grid()
plt.xlabel('Body Mass Index')
plt.ylabel('Life Expectancy')
plt.title ('Body Mass Index and Life Expectancy')

# Data load from clean csv file
# - loaded only two relevent columns
# - deleted rows with empty data
# - deleted rows with BMI below 10 or above 40
dataset=np.loadtxt('data_bmi_life.csv', delimiter=',')
y=dataset[:,1]
x=dataset[:,0]
plt.xlim([0,np.max(x) + 5])
plt.ylim([0,np.max(y) + 10])

# Calculations of m and b with printings
avg_x = np.mean(x)
print("avg_x= ", avg_x)
avg_y=np.mean(y)
print("avg_y= ", avg_y)

m=np.sum((x-avg_x)*(y-avg_y))/np.sum((x-avg_x)**2)
print("m= ", m)
b= avg_y-avg_x*m
print("b= " , b)

# Line drawing
x1=np.min(x)+2.0
y1=m*x1+b

x2=np.max(x)+2.0
y2=m*x2+b
plt.plot((x1,x2),(y1,y2))

# New data value calculation
new_x=float(input("enter your body mass index: "))
new_y=m*new_x+b
print('Expected Life in years : ' , new_y)
plt.scatter(new_x, new_y, color='r', marker ='*', s=40)

plt.scatter(x, y, color="g", marker="o", s=0.1)
plt.show()


