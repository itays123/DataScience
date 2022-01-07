import numpy as np

x1 = np.array([ [1] , [2] , [3] , [4] , [5 ], [6 ] ])
x2 = np.array([ [7] , [8] , [9] , [10] ,[11], [12] ])
x3 = np.array([ [13], [14], [15], [16], [17], [18] ])

merge = np.concatenate((x1, x2, x3))
print(merge)

merge1 = np.concatenate((x1, x2, x3), axis=1)
print(merge1)

merge2 = np.array((merge1[0], merge1[1], merge1[2]))
print(merge2)

arr1 = np.split(x1, 2);
arr2 = np.split(x2, 2);
arr3 = np.split(x3, 2);
merge3 = np.concatenate((arr1, arr2, arr3))
merge3 = np.array_split(merge3, 2)
print(np.array(merge3))