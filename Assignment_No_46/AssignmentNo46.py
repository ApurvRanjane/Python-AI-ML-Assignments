import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousRegression(Datapath):
    Border = "-"*40
    #Step 1:Load the data
    print(Border)
    print("Step 1:Load the data")
    print(Border)

    df = pd.read_csv(Datapath)
    print(df.head())

    #Step 2:Remove unwanted columns
    print(Border)
    print("Step 2:Remove unwanted columns")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    #Step 3:Check Missing values
    print(Border)
    print("Step 3:Check Missing values")
    print(Border)

    print("Total missing values : ")
    print(Border)
    print(df.isnull().sum())

    #Step 4:Statistical Summary
    print(Border)
    print("Step 4:Statistical Summary")
    print(Border)

    print(df.describe())

    #Step 5:Correlation
    print(Border)
    print("Step 5:Correlation")
    print(Border)

    print(df.corr())

    #Step 6: Seperate independent and dependent variables
    print(Border)
    print("Step 6: Split independent and dependent variables")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent variables: ")
    print(X.head())

    print("Dependent variables: ")
    print(Y.head())

    #Step 7: Split the dataset
    print(Border)
    print("Step 7: Split the dataset")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
        )

    print("Training Data:",X_train.shape)
    print("Testing Data:",X_test.shape)

    #Step 8:Create and train the model
    print(Border)
    print("Step 8:Create and train the model")
    print(Border)

    model = LinearRegression()
    model = model.fit(X_train,Y_train)

    print("Model Trained Successfully")

    #Step 9:test the model
    print(Border)
    print("Step 9:test the model")
    print(Border)

    Y_pred = model.predict(X_test)
    print("Expected Answers: ")
    print(Y_test[:3])

    print("Predicted answers: ")
    print(Y_pred[:3])

    #Step 10:Evaluate the model
    print(Border)
    print("Step 10:Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test,Y_pred)

    print("MSE : ",MSE)
    print("RMSE : ",RMSE)
    print("R2 : ",R2)

    #Step 11:Display Coiefficiect
    print(Border)
    print("Step 11:Display Coiefficiect")
    print(Border)

    print("TV Coiefficient: ",model.coef_[0])
    print("Radio Coiefficient: ",model.coef_[1])
    print("NewsPaper Coiefficient: ",model.coef_[2])

    print("Intercept : ",model.intercept_)
    
def main():
    MarvellousRegression("Advertising.csv")

if __name__=="__main__":
    main()