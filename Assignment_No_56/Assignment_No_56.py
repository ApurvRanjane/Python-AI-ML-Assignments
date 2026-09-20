# =========================================================
# Machine Learning Assignment
# Fraudulent Transaction Detection
# =========================================================

# A financial institution wants to detect potentially
# fraudulent transactions.

# Available information includes:
# • Transaction Amount
# • Transaction Time
# • Account Age
# • Number of Previous Transactions
# • Location Difference
# • Device Type
# • Failed Login Attempts

# Target:
# Fraud
# • 0 → Normal Transaction
# • 1 → Fraudulent Transaction

# You must investigate different ensemble approaches
# and recommend the most suitable model.

# Tasks

# Build and compare:
# 1. Decision Tree
# 2. Bagging Classifier
# 3. Random Forest Classifier
# 4. AdaBoost Classifier
# 5. Voting Classifier

# Evaluate each model using:
# • Accuracy
# • Precision
# • Recall
# • F1 Score
# • Confusion Matrix

# Prepare a final comparison:

# ---------------------------------------------------------
# | Algorithm      | Accuracy | Precision | Recall | F1 |
# ---------------------------------------------------------
# | Decision Tree  |          |           |        |    |
# | Bagging        |          |           |        |    |
# | Random Forest  |          |           |        |    |
# | AdaBoost       |          |           |        |    |
# | Voting         |          |           |        |    |
# ---------------------------------------------------------

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

#---------------------------------------------------------
#Step 1 : Load the dataset
#---------------------------------------------------------

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")
print("Shape of dataset : ",df.shape)
print("First 5 records : ")
print(df.head())
print("Missing Values : ")
print(df.isnull().sum())

#---------------------------------------------------------
#Step 2 : Seperate features and labels
#---------------------------------------------------------

X = df.drop("Fraud",axis=1)
Y = df["Fraud"]

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

dt = DecisionTreeClassifier(random_state=42)

bag = BaggingClassifier(estimator=dt,n_estimators=10,random_state=42)

rf = RandomForestClassifier(n_estimators=10,random_state=42)

ada = AdaBoostClassifier(n_estimators=50,learning_rate=1.0,random_state=42)

voting = VotingClassifier(
    estimators=[('dt',dt),('bag',bag),('rf',rf),('ada',ada)],
    voting='hard'
)

#---------------------------------------------------------
#Step 5.2 : Train the Individual Model
#---------------------------------------------------------

dt = dt.fit(X_train,Y_train)
bag = bag.fit(X_train,Y_train)
rf = rf.fit(X_train,Y_train)
ada = ada.fit(X_train,Y_train)
voting = voting.fit(X_train,Y_train)

#---------------------------------------------------------
#Step 5.3 : Test the Individual Model
#---------------------------------------------------------

dt_pred = dt.predict(X_test)
bag_pred = bag.predict(X_test)
rf_pred = rf.predict(X_test)
ada_pred = ada.predict(X_test)
voting_pred = voting.predict(X_test)

#---------------------------------------------------------
#Step 5.4 : Evaluate the Individual Model
#---------------------------------------------------------

dt_accuracy = accuracy_score(Y_test,dt_pred)
bag_accuracy = accuracy_score(Y_test,bag_pred)
rf_accuracy = accuracy_score(Y_test,rf_pred)
ada_accuracy = accuracy_score(Y_test,ada_pred)
voting_accuracy = accuracy_score(Y_test,voting_pred)

print("The Accuracy of Decision Tree Model is : ",dt_accuracy*100)
dt_precision = precision_score(Y_test, dt_pred)
dt_recall = recall_score(Y_test, dt_pred)
dt_f1 = f1_score(Y_test, dt_pred)
dt_cm = confusion_matrix(Y_test, dt_pred)

print("The Accuracy of Baggibg Classifier Model is : ",bag_accuracy*100)
bag_precision = precision_score(Y_test, bag_pred)
bag_recall = recall_score(Y_test, bag_pred)
bag_f1 = f1_score(Y_test, bag_pred)
bag_cm = confusion_matrix(Y_test, bag_pred)

print("The Accuracy of Random Forest Model is : ",rf_accuracy*100)
rf_precision = precision_score(Y_test, rf_pred)
rf_recall = recall_score(Y_test, rf_pred)
rf_f1 = f1_score(Y_test, rf_pred)
rf_cm = confusion_matrix(Y_test, rf_pred)

print("The Accuracy of AdaBoost Classifier Model is : ",ada_accuracy*100)
ada_precision = precision_score(Y_test, ada_pred)
ada_recall = recall_score(Y_test, ada_pred)
ada_f1 = f1_score(Y_test, ada_pred)
ada_cm = confusion_matrix(Y_test, ada_pred)

print("The Accuracy of Voting Classifier Model is : ",voting_accuracy*100)
voting_precision = precision_score(Y_test, voting_pred)
voting_recall = recall_score(Y_test, voting_pred)
voting_f1 = f1_score(Y_test, voting_pred)
voting_cm = confusion_matrix(Y_test, voting_pred)


print("\nDecision Tree Results")
print("Accuracy  :", dt_accuracy * 100)
print("Precision :", dt_precision)
print("Recall    :", dt_recall)
print("F1 Score  :", dt_f1)
print("Confusion Matrix :")
print(dt_cm)

print("\nBagging Classifier Results")
print("Accuracy  :", bag_accuracy * 100)
print("Precision :", bag_precision)
print("Recall    :", bag_recall)
print("F1 Score  :", bag_f1)
print("Confusion Matrix :")
print(bag_cm)

print("\nRandom Forest Results")
print("Accuracy  :", rf_accuracy * 100)
print("Precision :", rf_precision)
print("Recall    :", rf_recall)
print("F1 Score  :", rf_f1)
print("Confusion Matrix :")
print(rf_cm)

print("\nAdaBoost Results")
print("Accuracy  :", ada_accuracy * 100)
print("Precision :", ada_precision)
print("Recall    :", ada_recall)
print("F1 Score  :", ada_f1)
print("Confusion Matrix :")
print(ada_cm)

print("\nVoting Classifier Results")
print("Accuracy  :", voting_accuracy * 100)
print("Precision :", voting_precision)
print("Recall    :", voting_recall)
print("F1 Score  :", voting_f1)
print("Confusion Matrix :")
print(voting_cm)









