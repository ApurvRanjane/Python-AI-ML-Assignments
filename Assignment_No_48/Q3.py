# Q. Create a simple linear regression model using the following dataset:
# Years of Experience = [1, 2, 3, 4, 5]
# Salary = [20000, 25000, 30000, 35000, 40000]
#
# Predict the salary for a person with 6 years of experience.
# Plot the regression line and data points using matplotlib.

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([20000,25000,30000,35000,40000])

model = LinearRegression()

model.fit(X,Y)

print("Predicted Salary for 6 years of experienec is:",model.predict([[6]]))

#Visualization Part

# Slope and Intercept
m = model.coef_[0]
c = model.intercept_

# Regression Line
x = np.linspace(1, 6, 100)
y = c + m * x

plt.plot(x, y, color='g', label="Regression Line")
plt.scatter(X, Y, color='r', label="Data Points")

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)

plt.show()