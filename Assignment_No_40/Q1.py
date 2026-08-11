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

# Q1 ----------------------------------------------------
# After training the Decision Tree model, use:
# model.feature_importances_
#
# - Display importance score of each feature.
# - Which feature contributes the most in predicting FinalResult?
# - Which feature contributes the least?

importance = model.feature_importances_

for i in range(len(feature_cols)):
    print(feature_cols[i],":",importance[i])

most_index = importance.argmax()
min_index = importance.argmin()

print("\nFeatures contributing the most: ",feature_cols[most_index])
print("\nFeatures contributing the least: ",feature_cols[min_index])