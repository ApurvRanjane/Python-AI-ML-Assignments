# --------------------------------------------------
# Question 2
# --------------------------------------------------
# 2. The value of K plays an important role in the KNN algorithm.
#
# Write a Python program that demonstrates how prediction
# changes when K changes.
#
# Dataset:
#
# Use the same dataset as Question 1.
#
# Tasks:
# Predict the class of the same new point using:
#
# - K = 1
# - K = 3
# - K = 5
#
# Expected Output:
#
# Prediction Results
#
# K = 1 -> Red
# K = 3 -> Red
# K = 5 -> Blue
#
# Explain why the prediction changes when K increases.

import math

def MarvellousEucDistance(P1,P2):
    ans = math.sqrt((P1['X']-P2['X'])**2+(P1['Y']-P2['Y'])**2)
    return ans


def MarvellousKNNClassifier():
    Border = "-"*30

    Data = [
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':3,'Y':1,'label':'Blue'},
        {'point':'D','X':6,'Y':5,'label':'Blue'}
    ]

    print(Border)
    X_value = int(input("Enter X co-ordinate of new point: "))
    Y_value = int(input("Enter Y co-ordinate of new point: "))
    new_point = {'X':X_value,'Y':Y_value}

    print("Distances of all points")
    print(Border)
    for d in Data:
        d['distance'] =  MarvellousEucDistance(d,new_point)

    for d in Data:
        print(d)

    print(Border)

    sorted_data = sorted(Data,key=lambda item : item['distance'])

    K_values = [1,3,5]

    #The dataset contains only 4 training points, so K=5 is theoretically invalid.
    #In this implementation Python returns all available points, allowing the voting process to continue for demonstration purposes.
    
    for K in K_values:
        nearest = sorted_data[:K]

        #Voting
        votes = {}

        for neighbours in nearest:
            label = neighbours["label"]
            votes[label]=votes.get(label,0)+1

        imax = 0
        Name = ""

        for d in votes:
            if(votes[d]>imax):
                imax = votes[d]
                Name = d

        print(f"Final Prediction (K={K}) is: ",Name)

def main():
    MarvellousKNNClassifier()

if __name__=="__main__":
    main()