import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix)

# Q1 ----------------------------------------------------
# Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().

df = pd.read_csv("student_performance_ml.csv")

feature_cols = [
    "StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier(max_depth=5)

model.fit(X_train,Y_train)

# Q2 ----------------------------------------------------
# Use the trained model to predict results for X_test.
# Display predicted values along with actual values.

Y_pred = model.predict(X_test)
print("Actual Values : ",Y_test)
print("Predicted values : ",Y_pred)

# Q3 ----------------------------------------------------
# Calculate model accuracy using accuracy_score.
# Display the result in percentage format.
accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is: ",accuracy*100)

# Q4 ----------------------------------------------------
# Generate confusion matrix using sklearn.
# Display it using ConfusionMatrixDisplay.

cm = confusion_matrix(Y_test,Y_pred)
print("Confuion matrix of model is: ",cm)

# Q5 ----------------------------------------------------
# Calculate:
# - Training accuracy
# - Testing accuracy
#
# Compare both and comment whether the model is
# overfitting or underfitting.

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_acc = accuracy_score(Y_train,train_pred)
test_acc = accuracy_score(Y_test,test_pred)

print("Training Accuracy is : ",train_acc*100)
print("Testing Accuracy is : ",test_acc*100)

#Training Accuracy = 100% and Testing Accuracy = 100%. Since both accuracies are equal and very high, the model is neither overfitting nor underfitting and performs perfectly on the given dataset.

# Q6 ----------------------------------------------------
# Train three Decision Tree models with:
# - max_depth = 1
# - max_depth = 3
# - max_depth = None
#
# Compare their testing accuracies and write
# your observations.

depths = [1,3,None]

for d in depths:
    model = DecisionTreeClassifier(max_depth=d)
    model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test,Y_pred)
    print(f"Accuracy of model with depth {d} is: {accuracy*100}")

# Q7 ----------------------------------------------------
# Use the trained model to predict result for a student with:
# - StudyHours = 6
# - Attendance = 85
# - PreviousScore = 66
# - AssignmentsCompleted = 7
# - SleepHours = 7
#
# Will the student Pass or Fail?

new_student = [[6, 85, 66, 7, 7]]
prediction = model.predict(new_student)
if(prediction[0]==1):
    print("The new student will be pass..")

else:
    print("The new student will be fail..")