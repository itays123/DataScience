|# Exercise 1
import matplotlib.pyplot as plt
x=[]
y1=[]
y2=[]
for i in range(0, 30):
    x.append(i)
    y1.append(pow(x[i],2))
    y2.append(pow(x[i],3))
print(x)
print(y1)
print(y2)
