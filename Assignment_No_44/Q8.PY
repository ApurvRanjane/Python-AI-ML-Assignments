# Q8: Plot a line chart of marks for 'Amit' across all subjects.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

print("Shape of DataFrame: ",df.shape)
print("Names of columns : ",df.columns)
print("Data type of columns are : ",df.dtypes)

print(df.describe())

df['Total'] = df['Math']+df['Science']+df['English']

print(df)

print("Students Score 85+ marks in Science are :")
print(df[df['Science']>85])

print("Change Name Pooja to Puja..")
df['Name'] = df['Name'].replace("Pooja","Puja")
print(df)

print("Sort Dataframe by 'Total' marks in descending order: ")
df_sorted = df.sort_values(by='Total',ascending=False)
print(df_sorted)

plt.bar(df['Name'],df['Total'])
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.title("Name v/s Marks")
plt.show()

#Q8 answer
Amit_Marks = df[df['Name']=="Amit"][['Math','Science','English']].iloc[0]
plt.plot(['Math','Science','English'],Amit_Marks,marker = 'o')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks of Amit across all subjects")
plt.show()

