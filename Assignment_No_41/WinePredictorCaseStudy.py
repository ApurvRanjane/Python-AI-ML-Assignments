#Assignment No 41 is WinePredictor Case Study

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def WineClassifier(DataPath):
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

    print("Shape of Dataset : ",df.shape)
    print("Total Records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    print(Border)

    #Step 3 : Seperate independent and dependent variables

    print(Border)
    print("Step3: Seperate independent and dependent variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    print(Border)
    print("Input columns: ",X.columns.to_list())
    print("Output columns: Class")
    print(Border)

    #Step 4 : Split dataset for training and testing
    print(Border)
    print("Step4: Split dataset for training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)
    print(Border)
    print("Details on training and testing data:")
    print("Shape of X_train: ",X_train.shape)
    print("Shape of X_test: ",X_test.shape)
    print("Shape of Y_train: ",Y_train.shape)
    print("Shape of Y_test: ",Y_test.shape)
    print(Border)

    #Step 5 : Feature Scaling
    print(Border)
    print("Step5: Feature Scaling")
    print(Border)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.transform(X_test)

    print("Feature scaling done...")
    print(Border)

    #Step 6 : HyperParameter Tuning
    print(Border)
    print("Step 6 : HyperParameter Tuning")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    best_accuracy = 0
    best_k = 0
    best_pred = None

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train_scaled,Y_train)

        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

        if accuracy>best_accuracy:
            best_accuracy = accuracy
            best_k = k
            best_pred = Y_pred

    print("Best K value: ",best_k)
    print("Best Accuracy : ",best_accuracy*100)

    print(Border)

    #Step 7 : Graphical representation
    print(Border)
    print("Step 7 :Graphical representation")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker="o")
    plt.title("K values V/S Accuracy")
    plt.xlabel("Value of K") 
    plt.ylabel("Accuracy")  
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show() 

    #Step 8 : Model Evaluation
    print(Border)
    print("Step 8 :Model Evaluation")
    print(Border)

    cm = confusion_matrix(Y_test,best_pred)
    print("Best K value: ",best_k)
    print("Best Accuracy : ",best_accuracy*100)

    print("\nConfusion Matrix")
    print(cm)

    print(Border)
    
def main():
    WineClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()