# Q8: Plot a histogram of math marks.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)
print(df)

#Q1 Answer
scaler = MinMaxScaler()
df['Math_Normalized'] = scaler.fit_transform(df[['Math']])
print(df)

#Q2 Answer
df['Gender'] = ['Male','Male','Female']
gender_encoded = pd.get_dummies(df,columns=['Gender'])
print(gender_encoded)

#Q3 Answer
print("Group students by gender and calculate average marks")
grouped = df.groupby('Gender')[['Math','Science','English']].mean()
print(grouped)

#Q4 Answer
sagar = df[df['Name'] == 'Sagar'].iloc[0]

marks = [sagar['Math'], sagar['Science'], sagar['English']]
subjects = ['Math', 'Science', 'English']

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Subject Marks of Sagar")
plt.show()

#Q5 Answer
df['Total'] = df['Math'] + df['Science'] + df['English']
df['Status'] = np.where(df['Total']>=250,'Pass','Fail')
print(df)

#Q6 Answer
passed_count = (df['Status']=='Pass').sum()
print("Stdents Passed : ",passed_count)

#Q7 Answer
df.to_csv("Student_Data.csv",index=False)
print("Student file exported successfully")

#Q8 Answer
plt.hist(df['Math'],bins=5)
plt.title("Histogram of math marks")
plt.xlabel("Math Marks")
plt.ylabel("Frequency")
plt.show()
