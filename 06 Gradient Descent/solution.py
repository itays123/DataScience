import numpy as np

# Load dataset from file
dataset=np.loadtxt('data.csv', delimiter=',')
advertising=dataset[:,1]
sales=dataset[:,2]

# Divide sales by constant for easier calculations, and consier it when giving new predictions
MILLIONS_IN_BILLION=1000
sales /= MILLIONS_IN_BILLION

# Core functionality
def GradientDescent(x,y,learning_rate = 0.01, epochs = 1000):
    m = 0
    b = 0
    print("x y guess error new_m, new_b")
    for _ in range(epochs):
        for i in range(len(x)):
            xi = x[i]
            yi = y[i]
            guess = m * xi + b
            error = guess - yi
            m = m - (error * xi) * learning_rate
            b = b - error * learning_rate
            print(xi, yi, guess, error, m, b)
    return m, b

# Calculate the cost
def CalculateCost(x,y,m,b):
    sumOfErrorsSquared = 0
    for i in range(len(x)):
        error = m * x[i] + b - y[i]
        sumOfErrorsSquared += (error **2)
    return sumOfErrorsSquared

# Calculate the effect of the advertisement budget over the sales
m, b = GradientDescent(advertising, sales)
print("m:", m, "b:", b, "COST:", CalculateCost(advertising, sales, m, b))
print("With one more million euros inversted, sales are expected to grow by " + str(m * MILLIONS_IN_BILLION) + " million euros")