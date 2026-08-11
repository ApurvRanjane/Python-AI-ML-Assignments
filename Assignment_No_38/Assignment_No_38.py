import pandas as pd
import matplotlib.pyplot as plt

# 1. Write a Python program to load the file student_performance_ml.csv using pandas.

# Display:
# - First 5 records
# - Last 5 records
# - Total number of rows and columns
# - List of column names
# - Data types of each column

df = pd.read_csv("student_performance_ml.csv")
print(df.head())
print(df.tail())
print("Number of rows and columns : ",df.shape)
print("Column Names: ",list(df.columns))
print("Data type of each column is: ")
print(df.dtypes)

# 2. Write a program to:
# - Display total number of students in the dataset
# - Count how many students Passed (FinalResult = 1)
# - Count how many students Failed (FinalResult = 0)

print("Total Number of students is: ",df.shape[0])

passed = df[df["FinalResult"] == 1].shape[0]
print("Total passed students are: ",passed)

failed = df[df["FinalResult"] == 0].shape[0]
print("Total failed students are: ",failed)

# 3. Using pandas functions, calculate and display:
# - Average StudyHours
# - Average Attendance
# - Maximum PreviousScore
# - Minimum SleepHours

print("Average of study hours of student is: ",df["StudyHours"].mean())

print("Average of Attendance of student is: ",df["Attendance"].mean())

print("Maximum previous score is: ",df["PreviousScore"].max())

print("Minimum SleepHours are: ",df["SleepHours"].min())

# 4. Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

result_count = df["FinalResult"].value_counts()
print(result_count)

percentage = df["FinalResult"].value_counts(normalize=True)*100
print("Percentage:")
print(percentage)

if abs(percentage[0]-percentage[1])<10:
    print("Dataset is balanced..")
else:
    print("Dataset is not balanced..")

# 5. Based on the dataset values, analyze whether:
# - Higher StudyHours increase the chance of passing.
# - Higher Attendance improves FinalResult.
# Write your observations in 4–5 lines.


print(df.groupby("FinalResult")[["StudyHours","Attendance"]].mean())
#Students who passed generally have higher average study hours.
#Students with higher attendance tend to pass more often.
#Lower study hours are associated with more failures.
#Attendance appears to positively influence the final result.
#Both study hours and attendance contribute to better performance.

# 6. Plot a histogram of StudyHours.
# Explain what the distribution tells you.

plt.hist(df["StudyHours"],bins = 10,edgecolor = "black")
plt.title("Histogram of study hours")
plt.xlabel("Study Hours")
plt.ylabel("No of students")
plt.show()

# 7. Create a scatter plot of:
# StudyHours vs PreviousScore
# Use different colors for Pass and Fail students.

colors = {0:"red",1:"green"}
plt.scatter(
    df["StudyHours"],
    df["PreviousScore"],
    c=df["FinalResult"].map(colors)
)

plt.xlabel("Study hours")
plt.ylabel("Previous score")
plt.title("Study hours v/s Previous score")
plt.show()

# 8. Draw a boxplot for Attendance.
# Identify if any outliers are present.

plt.boxplot(df["Attendance"])
plt.title("Attendence boxplot")
plt.ylabel("Attendence")
plt.show()

# 9. Create a plot showing the relationship between
# AssignmentsCompleted and FinalResult.
# Explain your observation.

plt.scatter(df["AssignmentsCompleted"],df["FinalResult"])
plt.xlabel("Assignments completed")
plt.ylabel("Final result")
plt.title("Assignment completed v/s Final result")
plt.show()

# 10. Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

plt.scatter(df["SleepHours"],df["FinalResult"])
plt.xlabel("Sleep Hours")
plt.ylabel("Final result")
plt.title("SleepHours v/s Final result")
plt.show()

