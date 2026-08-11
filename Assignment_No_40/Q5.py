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
print("Accuracy of model is by using sklearn accuracy_score: ",accuracy*100)

# Q5 ----------------------------------------------------
# Without using accuracy_score, manually calculate accuracy.
#
# Verify whether it matches sklearn accuracy.
correct = 0
for i in range(len(Y_test)):
    if Y_test.iloc[i] == Y_pred[i]:
        correct = correct+1

mannual_acc = (correct/len(Y_test))*100
print("Mannual accuracy is : ",mannual_acc)