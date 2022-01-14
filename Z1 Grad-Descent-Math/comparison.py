# Comparing two Gradient Descent algorithms
import numpy as np

def GradientDescent1(x,y, learning_rate=0.01, epochs=1000):
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

def GradientDescent2(x,y, learning_rate=0.01, epochs=1000):
    m = 0
    b = 0
    for _ in range(epochs):
        errors = m * x + b - y
        m = m - learning_rate * np.sum(errors * x)
        b = b - learning_rate * np.sum(errors)
    return m, b

def CalculateCost(m, b, x, y):
    errors = m * x + b - y
    return np.sum(errors ** 2)

# Use previous formula learned for control

def LineRegControl(x, y):
    avg_x = np.mean(x)
    avg_y = np.mean(y)
    m=np.sum((x-avg_x)*(y-avg_y))/np.sum((x-avg_x)**2)
    b = avg_y-avg_x*m
    return m, b

# Load data
dataset=np.loadtxt('edu_life.csv', delimiter=',')
y=dataset[:,0]
x=dataset[:,1]

# Devide by constant
CONSTANT = 100
x /= CONSTANT
y /= CONSTANT

# Calculate linear regression with both algorithms
m, b = LineRegControl(x, y)
cost = CalculateCost(m, b, x, y) * CONSTANT
m1, b1 = GradientDescent1(x, y, learning_rate=0.001, epochs=2000)
cost1 = CalculateCost(m1, b1, x, y) * CONSTANT
m2, b2 = GradientDescent2(x, y)
cost2 = CalculateCost(m2, b2, x, y) * CONSTANT

print("Original algorithm: ", "m=", m, "b=", b, "cost=", cost)
print("First algorithm: ", "m=", m1, "b=", b1, "cost=", cost1)
print("Second algorithm: ", "m=", m2, "b=", b2, "cost=", cost2)