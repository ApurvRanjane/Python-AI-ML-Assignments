# 7. Write a Python program using LinearRegression to train a regression model using the dataset below.
#
# +-------------+-------+
# | Study Hours | Marks |
# +-------------+-------+
# |      1      |  50   |
# |      2      |  55   |
# |      3      |  60   |
# |      4      |  65   |
# |      5      |  70   |
# +-------------+-------+
#
# Your program should:
# • Train the regression model
# • Print the coefficient
# • Print the intercept


import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([50,55,60,65,70])

model = LinearRegression()

model.fit(X,Y)

m = model.coef_[0]
c = model.intercept_

print("The coiefficient is : ",m)
print("The intercept is : ",c)