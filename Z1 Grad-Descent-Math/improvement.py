# Improvement - trying to create Gradient Descent functions for functions to the nth power
import numpy as np

def ImprovedGradientDescent(x, y, learning_rate=0.01, epochs=1000, max_pow=1):
    max_pow += 1 # 1st power: y=mx+b, 2 variables, 2nd: y = ax^2+bx+c, 3 variables, etc..
    coefficients = np.zeros((max_pow)) 
    for _ in range(epochs):
        for i in range(len(x)):
            xi = x[i]
            yi = y[i]
            # Calculate guess
            guess = 0
            for power in range(max_pow):
                guess += coefficients[power] * (xi ** power)
            # Calculate error and move variables accordingly
            error = guess - yi
            for power in range(max_pow):
                coefficients[power] = coefficients[power] - learning_rate * error * (xi ** power)
    return coefficients

# Calculate Cost for nth power
def CalculateCost(x, y, coefficients, constant=1):
    guesses = np.zeros(len(x))
    for power in range(len(coefficients)):
        guesses += coefficients[power] * (x ** power)
    errors = guesses - y
    return np.sum(errors ** 2) * constant

# Control linear regression
def LineReg(x, y):
    avg_x = np.mean(x)
    avg_y = np.mean(y)
    m=np.sum((x-avg_x)*(y-avg_y))/np.sum((x-avg_x)**2)
    b = avg_y-avg_x*m
    return m, b

# Load data
dataset=np.loadtxt('ads_sales.csv', delimiter=',')
y=dataset[:,2]
x=dataset[:,1]

# Devide by constant
CONSTANT = 100
x /= CONSTANT
y /= CONSTANT

# Calculate
# Control
m, b = LineReg(x, y) 
cost = CalculateCost(x, y, [b, m], CONSTANT)
print("Control: cost=", cost)

# First, Second, Third power
for power in [1,2,3]:
    coefficients = ImprovedGradientDescent(x,y, learning_rate=0.1, max_pow=power, epochs=2000 * power)
    cost = CalculateCost(x,y, coefficients, CONSTANT)
    print("Power=", power, "cost=", cost)