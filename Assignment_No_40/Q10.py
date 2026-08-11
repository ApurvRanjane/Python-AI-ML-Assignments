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

# Q10 ---------------------------------------------------
# Train model with:
# - max_depth = None
#
# Calculate:
# - Training accuracy
# - Testing accuracy
#
# If training accuracy is 100% but testing accuracy is lower,
# explain why this happens.
model = DecisionTreeClassifier(max_depth=None)
model.fit(X_train, Y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_acc = accuracy_score(Y_train, train_pred)
test_acc = accuracy_score(Y_test, test_pred)

print("Training Accuracy is :", train_acc * 100)
print("Testing Accuracy is :", test_acc * 100)