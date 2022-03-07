import math
import numpy as np

# Calculate distance between two points
def distance(p1: Tuple[float, float], p2: Tuple[float, float]):
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
def distanceVec(p1: np.array, p2: np.array):
    distanceVec = p1 - p2
    return math.sqrt(np.dot(distanceVec, distanceVec))


p1 = np.array([0, 0, 0])
p2 = np.array([2, 2, 1])

print("Distance: ", distanceVec(p1, p2))