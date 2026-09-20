# 8. Using the regression model created in the previous question,
# write a Python program to predict marks for 6 study hours
# and display the predicted value.

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

print("Predicted Marks for 6 years of study is:",model.predict([[6]]))