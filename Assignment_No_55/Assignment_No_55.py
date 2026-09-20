#---------------------------------------------------------
# Machine Learning Assignment
# Customer Loan Approval Using Voting Classification
#
# A bank wants to automate its loan approval process.
#
# The bank has historical information about customers such as:
#   - Age
#   - Income
#   - Credit Score
#   - Existing Loan
#   - Employment Experience
#   - Loan Amount
#
# The target column is:
#   LoanApproved
#
# where:
#   0 -> Loan Rejected
#   1 -> Loan Approved
#
# The bank does not want to depend on a single Machine Learning algorithm.
#
# Build a Voting Classifier using:
#   - Logistic Regression
#   - Decision Tree
#   - K-Nearest Neighbors
#
# Tasks:
# 1. Load the dataset.
# 2. Check for missing values.
# 3. Separate input and output variables.
# 4. Split the dataset into training and testing data.
# 5. Train Logistic Regression.
# 6. Train Decision Tree.
# 7. Train KNN.
# 8. Calculate the individual accuracy of all three algorithms.
# 9. Create a Hard Voting Classifier.
# 10. Calculate its accuracy.
# 11. Create a Soft Voting Classifier.
# 12. Calculate its accuracy.
# 13. Compare:
#
# +----------------------+----------+
# | Model                | Accuracy |
# +----------------------+----------+
# | Logistic Regression  |          |
# | Decision Tree        |          |
# | KNN                  |          |
# | Hard Voting          |          |
# | Soft Voting          |          |
# +----------------------+----------+
#---------------------------------------------------------

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
#---------------------------------------------------------
#Step 1 : Load the dataset
#---------------------------------------------------------

df = pd.read_csv("Customer_Loan_Approval.csv")
print("Shape of dataset : ",df.shape)
print("First 5 records : ")
print(df.head())
print("Missing Values : ")
print(df.isnull().sum())

#---------------------------------------------------------
#Step 2 : Seperate features and labels
#---------------------------------------------------------

X = df.drop("LoanApproved",axis=1)
Y = df["LoanApproved"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

#---------------------------------------------------------
#Step 3 : Split dataset for training and testing
#---------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#---------------------------------------------------------
#Step 4 : Scale the features
#---------------------------------------------------------

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

#---------------------------------------------------------
#Step 5.1 : Create the Individual Models
#---------------------------------------------------------

model_log = LogisticRegression(max_iter=1000)

model_det = DecisionTreeClassifier(random_state=42)

model_knn = KNeighborsClassifier(n_neighbors=5)

#---------------------------------------------------------
#Step 5.2 : Train the Individual Model
#---------------------------------------------------------

model_log = model_log.fit(X_train,Y_train)
model_det = model_det.fit(X_train,Y_train)
model_knn = model_knn.fit(X_train,Y_train)

#---------------------------------------------------------
#Step 5.3 : Test the Individual Model
#---------------------------------------------------------

log_pred = model_log.predict(X_test)
det_pred = model_det.predict(X_test)
knn_pred = model_knn.predict(X_test)

#---------------------------------------------------------
#Step 5.4 : Evaluate the Individual Model
#---------------------------------------------------------

log_accuracy = accuracy_score(Y_test,log_pred)
det_accuracy = accuracy_score(Y_test,det_pred)
knn_accuracy = accuracy_score(Y_test,knn_pred)

print("The Accuracy of Logistic regression Model is : ",log_accuracy*100)
print("The Accuracy of Decision Tree Model is : ",det_accuracy*100)
print("The Accuracy of KNN Model is : ",knn_accuracy*100)

#---------------------------------------------------------
#Step 5.5 : Create the Voting Model (Hard Voting)
#---------------------------------------------------------

model1 = VotingClassifier(
    estimators=[('logistic',model_log),('decision_tree',model_det),('knn',model_knn)],
    voting='hard'
)

#---------------------------------------------------------
#Step 5.6 : Create the Voting Model (Soft Voting)
#---------------------------------------------------------

model2 = VotingClassifier(
    estimators=[('logistic',model_log),('decision_tree',model_det),('knn',model_knn)],
    voting='soft'
)

#---------------------------------------------------------
#Step 6 : Train the voting models
#---------------------------------------------------------

model1 = model1.fit(X_train,Y_train)
model2 = model2.fit(X_train,Y_train)

#---------------------------------------------------------
#Step 7 : Test the voting models
#---------------------------------------------------------

Y_pred1 = model1.predict(X_test)
Y_pred2 = model2.predict(X_test)

#---------------------------------------------------------
#Step 8 : Evaluate the models
#---------------------------------------------------------

print("Accuracy of Hard Voting : ",accuracy_score(Y_test,Y_pred1)*100)
print("Accuracy of Soft Voting : ",accuracy_score(Y_test,Y_pred2)*100)

