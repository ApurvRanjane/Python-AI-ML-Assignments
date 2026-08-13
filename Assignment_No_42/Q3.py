# --------------------------------------------------
# Question 3
# --------------------------------------------------
# 3. Use KNN to predict whether a student passes or fails
# based on study hours and attendance.
#
# Dataset:
#
# Study Hours | Attendance | Result
# 2           | 60         | Fail
# 5           | 80         | Pass
# 6           | 85         | Pass
# 1           | 50         | Fail
#
# Tasks:
# 1. Accept input from user:
#    - Study hours
#    - Attendance percentage
#
# 2. Apply KNN algorithm.
#
# 3. Predict whether the student Passes or Fails.
#
# Input Example:
#
# Enter Study Hours: 4
# Enter Attendance: 70
#
# Expected Output:
#
# Predicted Result: Pass

import math

def MarvellousEucDistance(P1,P2):
    ans = math.sqrt((P1['study_hrs']-P2['study_hrs'])**2+(P1['attendence']-P2['attendence'])**2)
    return ans

def MarvellousKNNClassifier(K=3):
    Border = "-"*30

    Data = [
        {'study_hrs': 2 ,'attendence': 60 ,'result': "Fail"},
        {'study_hrs': 5 ,'attendence': 80 ,'result': "Pass"},
        {'study_hrs': 6 ,'attendence': 85 ,'result': "Pass"},
        {'study_hrs': 1 ,'attendence': 50 ,'result': "Fail"}
    ]

    print(Border)
    s_hrs = int(input("Enter study hours of new student: "))
    attends = int(input("Enter attendence of new student: "))
    new_point = {'study_hrs':s_hrs,'attendence':attends}

    for d in Data:
        d['distance'] =  MarvellousEucDistance(d,new_point)

    sorted_data = sorted(Data,key=lambda item : item['distance'])

    nearest = sorted_data[:K]

    #Voting
    votes = {}

    for neighbours in nearest:
        result = neighbours["result"]
        votes[result]=votes.get(result,0)+1

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