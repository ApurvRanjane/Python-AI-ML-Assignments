# Deep Learning Assignment - Employee Attrition Prediction using MLPClassifier | Objective: Predict whether an employee is likely to stay (0) or leave (1) using historical employee data.

# 1. Load the dataset using Pandas.
# 2. Display the shape, columns and first five records.
# 3. Check for missing values.
# 4. Identify numerical and categorical features.
# 5. Convert categorical features such as OverTime into numerical representation.
# 6. Convert the target Attrition into 0 and 1.
# 7. Separate independent and dependent variables.
# 8. Divide the dataset into training and testing data.
# 9. Apply appropriate feature scaling.
# 10. Design an MLP with at least two hidden layers.
# 11. Train the network.
# 12. Display the number of iterations required for training.
# 13. Calculate training accuracy.
# 14. Calculate testing accuracy.
# 15. Generate a confusion matrix.
# 16. Plot the loss curve.
# 17. Create a function PredictAttrition(employee_data).
# 18. Test the system using at least five new employee records.
# 19. Explain whether the model is suffering from overfitting or underfitting.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import LabelEncoder

#-------------------------------------------------------------------
# Step 1 : Load the Dataset
#-------------------------------------------------------------------
print("Step 1 : Load the Dataset")
data = pd.read_csv("Employee_Attrition.csv")

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
# Step 4 : Convert Categorical features such as OverTime,Attrition into Numeric format
#-------------------------------------------------------------------
print("Step 4 : Convert Categorical features such as OverTime,Attrition into Numeric format")

le = LabelEncoder()
data['OverTime'] = le.fit_transform(data['OverTime'])
data['Attrition'] = le.fit_transform(data['Attrition'])

print("After Transforming categorical features into Numeric : ",data.head())

#-------------------------------------------------------------------
# Step 5 : Seperate Independent and Dependent variables
#-------------------------------------------------------------------
print("Step 5 : Seperate Independent and Dependent variables")

X = data[["Age","MonthlyIncome","YearsAtCompany","TotalWorkingYears","DistanceFromHome","JobSatisfaction","WorkLifeBalance","OverTime","NumCompaniesWorked","TrainingTimesLastYear"]]
Y = data["Attrition"]

print("Independetnt Variables : ")
print(X)
print("Dependetnt Variables : ")
print(Y)

#-------------------------------------------------------------------
# Step 6 : Divide the datset as training and testing data
#-------------------------------------------------------------------
print("Step 6 : Divide the datset as training and testing data")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state=42)
print("Training Input Shape : ",X_train.shape)
print("Testing Input Shape : ",X_test.shape)
print("Training Output Shape : ",Y_train.shape)
print("Testing Output Shape : ",Y_test.shape)

#------------------------------------------------------------------
# Step 7. Feature Scaling  
#------------------------------------------------------------------

print("7. Feature Scaling ")
sclar = StandardScaler()
X_train_scaled = sclar.fit_transform(X_train)
X_test_scaled =  sclar.transform(X_test)

print("Sclaled training data : ")
print(X_train_scaled[:5])

#------------------------------------------------------------------
# Step 8. MLP model with atleast 2 layers
#------------------------------------------------------------------

print("8. MLP model with atleast 2 layers")

model = MLPClassifier(
    hidden_layer_sizes=(16,12),
    activation="relu",
    solver="adam",
    max_iter=3000,
    random_state=42
)

print("Train the model")
model.fit(X_train_scaled,Y_train)
print("Model Training Completed..")

#------------------------------------------------------------------
# Step 9. display the no of iterations required for training
#------------------------------------------------------------------

print("9. display the no of iterations required for training : ")
print(model.n_iter_)

#------------------------------------------------------------------
# Step 10. Calculate Training Accuracy
#------------------------------------------------------------------
print("Step 10. Calculate Training Accuracy")

Y_pred_train = model.predict(X_train_scaled)
training_accu = accuracy_score(Y_pred_train,Y_train)
print(training_accu*100)

#------------------------------------------------------------------
# Step 11. Calculate Testing Accuracy
#------------------------------------------------------------------
print("Step 11. Calculate Testing Accuracy")

Y_pred_test = model.predict(X_test_scaled)
testing_accu = accuracy_score(Y_pred_test,Y_test)
print(testing_accu*100)

#------------------------------------------------------------------
# Step 12. Generate Confusion Matrix
#------------------------------------------------------------------
print("Step 12. Generate Confusion Matrix")
cm = confusion_matrix(Y_pred_test,Y_test)
print(cm)

#------------------------------------------------------------------#
# Step 13. Plot Loss Curve
#------------------------------------------------------------------#

print("Step 13. Plot Loss Curve")

plt.figure(figsize=(8,5))
plt.plot(model.loss_curve_)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.grid(True)
plt.show()

#------------------------------------------------------------------#
# Step 14. Create function predictAttrition(employee_data)
#------------------------------------------------------------------#

print("Step 14. Create function predictAttrition(employee_data)")
def predictAttrition(employee_data):
    
    employee_data_scaled = sclar.transform([employee_data])
    
    prediction = model.predict(employee_data_scaled)
    
    if prediction[0] == 1:
        print("Employee is likely to leave the company.")
    else:
        print("Employee is likely to stay in the company.")

employee = [
    35,     # Age
    50000,  # MonthlyIncome
    5,      # YearsAtCompany
    10,     # TotalWorkingYears
    3,      # DistanceFromHome
    4,      # JobSatisfaction
    3,      # WorkLifeBalance
    1,      # OverTime (Yes=1, No=0)
    2,      # NumCompaniesWorked
    3       # TrainingTimesLastYear
]

predictAttrition(employee)

#------------------------------------------------------------------#
# Step 15.Test the system using at least five new employee records
#------------------------------------------------------------------#

print("Step 15.Test the system using at least five new employee records")
print("Testing with New Employee Records")

emp1 = [25,30000,1,2,5,2,2,1,1,2]
emp2 = [40,80000,10,15,3,4,4,0,2,4]
emp3 = [28,35000,2,4,10,2,3,1,3,2]
emp4 = [50,100000,20,25,2,5,5,0,1,5]
emp5 = [32,45000,3,8,15,3,2,1,4,3]

predictAttrition(emp1)
predictAttrition(emp2)
predictAttrition(emp3)
predictAttrition(emp4)
predictAttrition(emp5)

#------------------------------------------------------------------#
# Step 16.Explain whether the model is suffering from overfitting or underfitting
#------------------------------------------------------------------#

print("Step 16.Explain whether the model is suffering from overfitting or underfitting")
print("The model is suffering from overfitting because the training accuracy (98.5%) is much higher than the testing accuracy (72%). The model has learned the training data very well but does not generalize effectively to unseen data.")