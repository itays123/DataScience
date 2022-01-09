# Exercise 9 - working with pixel arrays
import numpy as np
import matplotlib.pyplot as plt

picture = np.zeros((100, 100, 3), dtype=np.uint8)

picture[0:50, 0:50, 0] = 255 # Set red to 255 in those indexes 
picture[50:100, 0:50, 1] = 255 # Set green to 255 in those indexes
picture[0:50, 50:100, 2] = 255 # Set blue to 255 in those indexes
picture[50:100, 50:100, :] = 255 # Set everything to 255 in those indexes

plt.imshow(picture, interpolation='nearest')
plt.show()