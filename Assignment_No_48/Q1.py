# Q1. Implement Simple Linear Regression manually without using any ML library.
#
# Dataset
# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]
#
# Tasks:
# 1. Calculate Mean of X
# 2. Calculate Mean of Y
# 3. Calculate Slope (m)
# 4. Calculate Intercept (c)
#
# Expected Output:
# Mean of X = 3
# Mean of Y = 3.6
# Slope (m) = 0.4
# Intercept (c) = 2.4
#
# Regression Equation:
# Y = 0.4X + 2.4
#
# Predicted Y for X = 6 : 4.8

import pandas as pd
import numpy as np

#Load the Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

X_mean = 0
Y_mean = 0

for i in range(len(X)):
    X_mean = X_mean + X[i]
    Y_mean = Y_mean + Y[i]

n = len(X)

X_mean = X_mean/n
Y_mean = Y_mean/n

print("mean of X is : ",X_mean)
print("mean of Y is : ",Y_mean)

Denominator = 0
Numerator = 0

for i in range(n):
    Numerator = Numerator + ((X[i]-X_mean)*(Y[i]-Y_mean))
    Denominator = Denominator+((X[i]-X_mean)**2)

slope = Numerator/Denominator
print("Slope of line is : ",slope)

#y = mx+c
#c = y-mx
#c = y_mean - m*x_mean

C = Y_mean - (slope*X_mean)
print("Y-Intercept of line is : ",C)

print(f"The regression equation of line is : Y = {slope}X + {C} ")

trial = 6
print("Predicted Y for 6: ",slope*trial + C)


