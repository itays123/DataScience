# Calculate Eucledian distance between points and calculate things with it
from enum import unique
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Calculate distance between two points
def distance(p1, p2):
    deltaX = p1[0] - p2[0]
    deltaY = p1[1] - p2[1]
    return math.sqrt(deltaX ** 2 + deltaY ** 2)

# Read a point
def readPoint():
    x = float(input("Enter x value: "))
    y = float(input("Enter y value: "))
    return x, y

# p1 = readPoint()
# p2 = readPoint()
# print("Distance: ", distance(p1, p2))

# Calculate the distance between two multi-dimensional points
def distanceVec(p1: np.array, p2: np.array, axis = 0):
    distanceVec = p1 - p2
    return np.linalg.norm(distanceVec, axis=axis) # mathematical length of vector


# p1 = np.array([0, 0, 0])
# p2 = np.array([2, 2, 1])
# print("Distance: ", distanceVec(p1, p2)) # 3.0

# scatter points on a 3D space
def scatterPoints(data, s = 150):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(data[:,0], data[:,1], data[:,2], s)
    plt.show()

# find indexes of the k closest points to a given point
def findKNextNeighbors(point, data, k=3):
    distances = distanceVec(point, data, axis=1)
    # get indexes of the k closest points 
    indexes = distances.argsort()[:k]
    return indexes


train_data = np.array( [
    [ 2.0 , 3.0 ],
    [ 3.0 , 7.0 ],
    [ 4.0 , 4.0 ],
    [ 5.0 , 8.0 ],
    [ 6.0 , 5.0 ],
    [ 7.0 , 9.0 ],
    [ 8.0 , 5.0 ],
    [ 8.0 , 2.0 ],
    [10.0 , 2.0 ] 
])

train_lbl = np.array( [
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 2 ],
    [ 2 ],
    [ 2 ],
    [ 2 ],
    [ 2 ] 
])

test_data = np.array([[ 6.0 , 7.0 ]])

# expected for k=3: [[5. 8.]  [6. 5.]  [7. 9.]]
# expected for k=1: [[5. 8.]]
# print(train_data[findKNextNeighbors(test_data, train_data)]) 

# predict label of an input point based on the KNN algorithm
def predict(point, data, labels, k=3):
    knnIndexes = findKNextNeighbors(point, data, k)
    knnLabels = labels[knnIndexes]
    # get unique values and the count of each in the labels
    values, counts = np.unique(knnLabels, return_counts=True)
    freqIndex = np.argmax(counts)
    return values[freqIndex]

# expected for k=3: 2
print(predict(test_data, train_data, train_lbl)) 
# expected for k=1: 1
print(predict(test_data, train_data, train_lbl, k=1)) 


