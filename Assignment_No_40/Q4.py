import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix)

df = pd.read_csv("student_performance_ml.csv")

feature_cols = [
    "StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier(max_depth=5,random_state=42)

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is: ",accuracy*100)

# Q4 ----------------------------------------------------
# Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.

new_students = pd.DataFrame({
    "StudyHours":[6,4,7,3,8],
    "Attendance":[85,60,90,55,84],
    "PreviousScore":[66,45,77,88,54],
    "AssignmentsCompleted":[7,5,8,4,9],
    "SleepHours":[7,6,8,5,7]
})

new_pred = model.predict(new_students)
print(new_pred)
