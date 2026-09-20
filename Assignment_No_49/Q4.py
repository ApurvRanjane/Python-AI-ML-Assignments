# 4. Write a Python program to calculate the Euclidean distance between two points before and after
# applying feature scaling, and explain the difference in results.

from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean
import numpy as np

data = np.array([
    [25,20000],
    [30,40000],
    [35,80000]
])

distance_before = euclidean(data[0],data[1])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

distance_after = euclidean(scaled_data[0],scaled_data[1])

print("Eucledian Distance before feature scaling = ",distance_before)
print("Eucledian Distance after feature scaling = ",distance_after)

#Before scaling, the salary feature dominates because its values are much larger.
#After scaling, all features have equal importance.
#Euclidean distance becomes more meaningful for machine learning algorithms.