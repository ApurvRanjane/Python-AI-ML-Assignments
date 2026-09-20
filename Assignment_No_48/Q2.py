# Q2. Using the same dataset from question 1, calculate model performance.
#
# Dataset
# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]
#
# Tasks:
# 1. Predict all Y values using regression equation.
# 2. Calculate:
#    - Mean Squared Error (MSE)
#    - R² Score
# 3. Show all intermediate calculations.


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

Y_Pred = []
for i in range(n):
    print(f"Actual value of Y for {X[i]} : {Y[i]}")
    ans = slope*X[i]+C
    Y_Pred.append(ans)
    print(f"Predicted Y value for {X[i]} : {ans}")
    print("")

#Mean sqaure error 
YP_mean = 0
for i in range(n):
    YP_mean = YP_mean + ((Y[i]-Y_Pred[i])**2)

MSE = (1/n)*(YP_mean)
print("Mean Squared Error is: ",MSE)

#R square error
SS_Result = YP_mean
SS_Total = 0

for i in range(n):
    SS_Total = SS_Total+((Y[i]-Y_mean)**2)

R_square = 1 - (SS_Result/SS_Total)

print("R square is : ",R_square)

