# Design machine learning application which follows below steps as
#
# Step 1:
# Get Data
# Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.
#
# Step 2:
# Clean, Prepare and Manipulate data
# As we want to use the above data into machine learning application we have prepare
# that in the format which is accepted by the algorithms.
# As our dataset contains two features as Wether and Temperature. We have to replace
# each string field into numeric constants by using LabelEncoder from processing
# module of sklearn.
#
# Step 3:
# Train Data
# Now we want to train our data for that we have to select the Machine learning algorithm.
# For that we select K Nearest Neighbour algorithm.
# use fit method for training purpose. For training use whole dataset.
#
# Step 4:
# Test Data
# After successful training now we can test our trained data by passing some value of
# wether and temperature.
# As we are using KNN algorithm use value of K as 3.
# After providing the values check the result and display on screen.
# Result may be Yes or No.
#
# Step 5:
# Calculate Accuracy
# Write one function as CheckAccuracy() which calculate the accuracy of our algorithm.
# For calculating the accuracy divide the dataset into two equal parts as Training data
# and Testing data.
# Calculate Accuracy by changing value of K.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

def MarvellousClassifier(DataPath):
    Border = "-"*40

    #Step 1 : Load the dataset from csv file

    print(Border)
    print("Step 1 : Load the dataset from csv file")
    print(Border)

    df = pd.read_csv(DataPath)

    print(Border)
    print("Some entries from Dataset : ")
    print(df.head())
    print(Border)

    #Step 2 : Clean the Dataset
    print(Border)
    print("Step 2 : Clean the Dataset")
    print(Border)

    df.dropna(inplace=True)
    df.drop(columns=['Unnamed: 0'], inplace=True)
    print("Shape of Dataset : ",df.shape)
    print("Total Records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    print(Border)

    #Step 3 : Encoding Categorical Variables
    
    print(Border)
    print("Step 3 : Encoding Categorical Variables")
    print(Border)

    weatherEncoder = LabelEncoder()
    tempEncoder = LabelEncoder()

    df["Wether"] = weatherEncoder.fit_transform(df["Wether"])
    df["Temperature"] = tempEncoder.fit_transform(df["Temperature"])


    #Step 4 : Seperate independent and dependent variables

    print(Border)
    print("Step4: Seperate independent and dependent variables")
    print(Border)

    X = df.drop(columns=['Play'])
    Y = df['Play']

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    print(Border)
    print("Input columns: ",X.columns.to_list())
    print("Output columns: Play")
    print(Border)

    #Step 5 : Build the model
    print(Border)
    print("Step 5 : Build the model")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)
    print("Classification model is created")

    #Step6 : Train the model
    print(Border)
    print("Step6 : Train the model")
    print(Border)

    model = model.fit(X,Y)
    print("Model training completed")
    print(Border)

    #Step7 : Test the model
    print(Border)
    print("Step7 : Test the model")
    print(Border)

    Weather = input("Enter Weather : ")
    Temp = input("Enter Temperature : ")

    Weather = weatherEncoder.transform([Weather])[0]
    Temp = tempEncoder.transform([Temp])[0]

    InputData = pd.DataFrame(
    [[Weather, Temp]],
    columns=['Wether', 'Temperature']
    )

    result = model.predict(InputData)

    print("Predicted Result :", result[0])

    #Step 8 : Split dataset for training and testing
    print(Border)
    print("Step8: Split dataset for training and testing")
    print(Border)
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)
    print(Border)
    print("Details on training and testing data:")
    print("Shape of X_train: ",X_train.shape)
    print("Shape of X_test: ",X_test.shape)
    print("Shape of Y_train: ",Y_train.shape)
    print("Shape of Y_test: ",Y_test.shape)
    print(Border)

    def AccuracyChecker(K):
        model = KNeighborsClassifier(n_neighbors=K)
        model = model.fit(X_train,Y_train)
        Y_Pred = model.predict(X_test)
        accuracy = accuracy_score(Y_Pred,Y_test)
        print(f"Accuracy of model when K={K}: {accuracy*100}")

    for k in range(1,16):
        AccuracyChecker(k)

def main():
    MarvellousClassifier("PlayPredictor.csv")

if __name__ == "__main__":
    main()