import numpy as np

# Load dataset from file
dataset=np.loadtxt('data.csv', delimiter=',')
advertising=dataset[:,1]
sales=dataset[:,2]

# Divide sales by constant for easier calculations, and consier it when giving new predictions
CONSTANT=100
sales /= CONSTANT
advertising /= CONSTANT

# Core functionality
def GradientDescent(x,y,learning_rate = 0.01, epochs = 1000):
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

# Calculate the cost
def CalculateCost(x,y,m,b):
    errors = m * x + b - y
    return np.sum(errors ** 2)

# Calculate the effect of the advertisement budget over the sales
m, b = GradientDescent(advertising, sales)
print("m:", m, "b:", b, "COST:", CalculateCost(advertising, sales, m, b))
print("With one more million euros inversted, sales are expected to grow by " + str(m) + " million euros")