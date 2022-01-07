# Exercise 6 - common elements
import numpy as np

arr1 = np.arange(0, 100, 2)
print('arr1', arr1)
arr2 = np.arange(0, 100, 3)
print('arr2', arr2)
common = np.intersect1d(arr1, arr2)
print('Common elements', common)
