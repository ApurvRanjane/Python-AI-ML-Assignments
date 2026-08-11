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

# Q2 ----------------------------------------------------
# Remove the column SleepHours from the dataset.
#
# - Train the model again.
# - Compare new accuracy with previous accuracy.
# - Does removing this feature affect performance?

X_new = X.drop("SleepHours",axis=1)
X_train,X_test,Y_train,Y_test = train_test_split(X_new,Y,test_size=0.2,random_state=42)
model = DecisionTreeClassifier(max_depth=5)
model = model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
print("Accuracy after removing SleepHours Feature: ",accuracy_score(Y_test,Y_pred)*100)