import numpy as np

arr = [
    [(1, 11, 21), (3, 12, 22)],
    [(2, 3, 1), (4, 14, 24)]
]
arr = np.array(arr)
print(arr)

arr2 = arr * 2
arr3 = arr + 10
print(arr2)
print(arr3)