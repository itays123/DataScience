import matplotlib.pyplot as plt
import numpy as np

# Exercise 1

x= np.arange(0, 30, 1)
y1= x ** 2
y2= x ** 3
print(x)
print(y1)
print(y2)

# Exercise 2
# Create grid
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.grid()

x = np.arange(-3, 4, 1)
y = x ** 2

plt.xlim([np.min(x) - 1,np.max(x) + 1])
plt.ylim([np.min(y) - 1,np.max(y) + 1])

plt.plot(x, y)
plt.show()
