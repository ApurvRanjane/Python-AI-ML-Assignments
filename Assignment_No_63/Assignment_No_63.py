# ============================================================
# CASE STUDY : LOAN DEFAULT PREDICTION USING MLP CLASSIFIER
# ============================================================
# In this case study, a financial institution wants to predict
# whether a loan applicant is likely to default on a loan.
# The dataset contains applicant information such as Age,
# Income, Loan Amount, Credit Score, Employment Years,
# Existing Loans, Monthly Debt, Loan Term, Previous Default
# History, and Home Ownership status.
#
# A Multi-Layer Perceptron (MLP) Neural Network is used to
# learn patterns from historical loan records and classify
# applicants as Low Risk (No Default) or High Risk (Default).
# The objective is to help financial institutions make better
# loan approval decisions and reduce financial risk.
# ============================================================

# Q1. Load the Loan Default dataset and understand its structure.
# Q2. Perform exploratory data analysis (EDA) to understand the features and target variable.
# Q3. Check for missing values and handle them if necessary.
# Q4. Determine whether the target classes are balanced or imbalanced.
# Q5. Convert categorical features (PreviousDefault and HomeOwnership) into numeric values.
# Q6. Separate the dataset into independent variables (X) and dependent variable (Y).
# Q7. Split the dataset into training and testing sets using train_test_split().
# Q8. Why is stratified splitting important in classification problems?
# Q9. Apply feature scaling using StandardScaler.
# Q10. Create a Multi-Layer Perceptron (MLP) Classifier model.
# Q11. Train the MLP model using the training dataset.
# Q12. Evaluate the model using testing accuracy.
# Q13. Generate and interpret the confusion matrix.
# Q14. Generate the classification report.
# Q15. Calculate Precision, Recall, and F1-Score.
# Q16. Plot the training loss curve and analyze convergence.
# Q17. Test the trained model on new loan applicant data and predict default risk.

# Hyperparameter Experiment 1:
# Compare different activation functions (identity, logistic, tanh, relu).

# Hyperparameter Experiment 2:
# Compare different hidden layer architectures.

# Hyperparameter Experiment 3:
# Compare different learning rates and analyze their impact on accuracy.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder

#-------------------------------------------------------------------
# Step 1 : Load the Dataset
#-------------------------------------------------------------------
print("Step 1 : Load the Dataset")
data = pd.read_csv("Loan_Default.csv")

#-------------------------------------------------------------------
# Step 2 : Data Analysis(EDA)
#-------------------------------------------------------------------
print("Step 2 : Data Analysis(EDA)")

print("Shape of data is : ",data.shape)
print("Column Names : ",data.columns)
print("first 5 samples in datset are : ",data.head())

#-------------------------------------------------------------------
# Step 3 : Check for Null values
#-------------------------------------------------------------------
print("Step 3 : Check for Null values")

print(data.isnull().sum())

#-------------------------------------------------------------------
# Step 4 : Check Target variables balanced or not balanced
#-------------------------------------------------------------------
print("Step 4 : Check Target variables balanced or not balanced")

print(data['Default'].value_counts())
print(data['Default'].value_counts(normalize=True)*100)

#-------------------------------------------------------------------
# Step 5 : Convert Categorical features into numeric
#-------------------------------------------------------------------
print("Step 5 : Convert Categorical features into numeric")

le = LabelEncoder()
data['PreviousDefault'] = le.fit_transform(data['PreviousDefault'])
data['HomeOwnership'] = le.fit_transform(data['HomeOwnership'])

print("After Transforming categorical features into Numeric : ",data.head())

#-------------------------------------------------------------------
# Step 6 : Seperate Independent and Dependent variables
#-------------------------------------------------------------------
print("Step 6 : Seperate Independent and Dependent variables")

X = data[["Age","Income","LoanAmount","CreditScore","EmploymentYears","ExistingLoans","MonthlyDebt","LoanTerm","PreviousDefault","HomeOwnership"]]
Y = data["Default"]

print("Independetnt Variables : ")
print(X)
print("Dependetnt Variables : ")
print(Y)

#-------------------------------------------------------------------
# Step 7 : Divide the datset as training and testing data
#-------------------------------------------------------------------
print("Step 7 : Divide the datset as training and testing data")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state=42,stratify=Y)
print("Training Input Shape : ",X_train.shape)
print("Testing Input Shape : ",X_test.shape)
print("Training Output Shape : ",Y_train.shape)
print("Testing Output Shape : ",Y_test.shape)

#------------------------------------------------------------------
# Step 8. Why Stratified Splitting?
#------------------------------------------------------------------

# It preserves class distribution in train and test sets.

#------------------------------------------------------------------
# Step 9. Feature Scaling  
#------------------------------------------------------------------

print("9. Feature Scaling ")
scalar = StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled =  scalar.transform(X_test)

print("Sclaled training data : ")
print(X_train_scaled[:5])

#------------------------------------------------------------------
# Step 10.Craete MLP model 
#------------------------------------------------------------------

print("10. Craete MLP model ")

model = MLPClassifier(
    hidden_layer_sizes=(32,16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

#------------------------------------------------------------------
# Step 11. Train the Model
#------------------------------------------------------------------
print("Step 11 : Train the model")
model.fit(X_train_scaled,Y_train)
print("Model Training Completed..")

#------------------------------------------------------------------
# Step 12. Calculate Testing Accuracy
#------------------------------------------------------------------
print("Step 11. Calculate Testing Accuracy")

Y_pred_test = model.predict(X_test_scaled)
testing_accu = accuracy_score(Y_pred_test,Y_test)
print(testing_accu*100)

#------------------------------------------------------------------
# Step 13. Generate Confusion Matrix
#------------------------------------------------------------------
print("Step 12. Generate Confusion Matrix")
cm = confusion_matrix(Y_pred_test,Y_test)
print(cm)

#------------------------------------------------------------------
# Step 14. Generate Classification Report
#------------------------------------------------------------------
print("Step 14. Generate Classification Report")
cr = classification_report(Y_pred_test,Y_test)
print("Classification Report:")
print(cr)

#------------------------------------------------------------------
# Step 15. Calculate Precision,Recall,F-1 score
#------------------------------------------------------------------

print("Step 15. Calculate Precision,Recall,F-1 score")
precison = precision_score(Y_pred_test,Y_test)
recall = recall_score(Y_pred_test,Y_test)
f1 = f1_score(Y_pred_test,Y_test)

print("Precision : ",precison)
print("Recall : ",recall)
print("F-1 Score : ",f1)

#------------------------------------------------------------------
# Step 16. Plot training loss
#------------------------------------------------------------------
print("Step 16. Plot training loss")

plt.plot(model.loss_curve_)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("Training Loss Curve")
plt.show()

#------------------------------------------------------------------
# 17. Test model on new loan applicants
#------------------------------------------------------------------
print("17. Test model on new loan applicants")

new_applicant = pd.DataFrame({
    'Age':[35],
    'Income':[60000],
    'LoanAmount':[15000],
    'CreditScore':[720],
    'EmploymentYears':[8],
    'ExistingLoans':[1],
    'MonthlyDebt':[500],
    'LoanTerm':[36],
    'PreviousDefault':[0],
    'HomeOwnership':[1]
})

new_scaled = scalar.transform(new_applicant)

prediction = model.predict(new_scaled)

if prediction[0] == 0:
    print("\nLow Default Risk")
else:
    print("\nHigh Default Risk")

#Hyperparameter Experiments
#Experiment 1 – Activation Functions

for act in ['identity','logistic','tanh','relu']:
    model = MLPClassifier(
    hidden_layer_sizes=(32,16),
    activation= act,
    solver="adam",
    max_iter=1000,
    random_state=42
    )

    model.fit(X_train_scaled,Y_train)

    pred = model.predict(X_test_scaled)

    print(act,
          accuracy_score(Y_test,pred)*100)
    
#Experiment 2 – Hidden Layers

layers = [
    (10,),
    (20,10),
    (50,25),
    (100,50,25)
]

for layer in layers:
    model = MLPClassifier(
        hidden_layer_sizes=layer,
        activation= 'relu',
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train_scaled,Y_train)
    
    pred = model.predict(X_test_scaled)
    
    print(layer,accuracy_score(Y_test,pred)*100)

#Experiment 3 – Learning Rate

for lr in [0.001,0.01,0.1]:
    model = MLPClassifier(
        hidden_layer_sizes=(32,16),
        activation='relu',
        learning_rate_init=lr,
        solver='adam',
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train_scaled,Y_train)

    pred = model.predict(X_test_scaled)

    print("LR =",lr,
          "Accuracy =",accuracy_score(Y_test,pred)*100)
    

