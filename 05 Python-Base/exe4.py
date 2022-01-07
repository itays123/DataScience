# Exercise 4 - measuring time
import time

# Measure list time
startTime = time.time()
list = [];
for i in range(1000000):
    list.append(i)
endTime = time.time()
print("Time taken for list:" , (endTime - startTime) , "seconds")

# Measure numpy array time
import numpy as np

startTime = time.time()
arr = np.arange(0, 1000000, 1)
endTime = time.time()
print("Time taken for array:" , (endTime - startTime) , "seconds")