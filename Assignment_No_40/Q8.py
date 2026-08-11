import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix)
import matplotlib.pyplot as plt

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

# Q8 ----------------------------------------------------
# Decision Tree Visualization
#
# Use:
# from sklearn.tree import plot_tree
#
# Visualize the trained decision tree.
#
# - Which feature appears at the root node?
# - Why do you think that feature was selected first?

plt.figure(figsize=(12,8))

plot_tree(
    model,
    feature_names=feature_cols,
    class_names=["Pass","Fail"],
    filled=True
)

plt.show()
