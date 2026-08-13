# --------------------------------------------------
# Question 1
# --------------------------------------------------
# 1. Write a Python program that classifies a new data point
# using the K-Nearest Neighbors algorithm.
# The algorithm should be implemented manually without using
# any machine learning library.
#
# The program should:
# - Calculate Euclidean distance
# - Sort distances
# - Select K nearest neighbors
# - Predict the class based on majority voting
#
# Dataset:
#
# Point | X | Y | Label
# A     | 1 | 2 | Red
# B     | 2 | 3 | Red
# C     | 3 | 1 | Blue
# D     | 5 | 5 | Blue
#
# Tasks:
# 1. Accept X and Y coordinates of a new point from the user.
# 2. Compute Euclidean distance from all dataset points.
# 3. Sort the distances.
# 4. Select K = 3 nearest neighbors.
# 5. Predict the class label.
#
# Input Format:
#
# Enter X coordinate: 2
# Enter Y coordinate: 2
#
# Expected Output:
#
# Nearest Neighbours:
# A - Distance: 1.0
# B - Distance: 1.0
# C - Distance: 1.41
#
# Predicted Class: Red

import math

def MarvellousEucDistance(P1,P2):
    ans = math.sqrt((P1['X']-P2['X'])**2+(P1['Y']-P2['Y'])**2)
    return ans


def MarvellousKNNClassifier(K=3):
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

    print("Final Prediction is: ",Name)

def main():
    MarvellousKNNClassifier()

if __name__=="__main__":
    main()