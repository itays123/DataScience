import numpy as np

x = np.arange(0, 9, 1)
y = np.array([1,4,2,5,7,8,8,9,10])

def GradientDescendent(x,y,learning_rate = 0.01, epochs = 1000):
    m = 0
    b = 0
    for _ in range(epochs):
        for i in range(len(x)):
            xi = x[i]
            yi = y[i]
            guess = m * xi + b
            error = guess - yi
            m = m - (error * xi) * learning_rate
            b = b - error * learning_rate
    return m, b