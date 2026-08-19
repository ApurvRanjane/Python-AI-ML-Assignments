# Q9: Create a DataFrame with missing values and fill them with column mean.

# data2 = {
#     'Name': ['Amit', 'Sagar', 'Pooja'],
#     'Math': [np.nan, 76, 88],
#     'Science': [91, np.nan, 85]
# }

import pandas as pd
import numpy as np
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

Amit_Marks = df[df['Name']=="Amit"][['Math','Science','English']].iloc[0]
plt.plot(['Math','Science','English'],Amit_Marks,marker = 'o')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks of Amit across all subjects")
plt.show()

#Q9 answer
data2 = {
     'Name': ['Amit', 'Sagar', 'Pooja'],
     'Math': [np.nan, 76, 88],
     'Science': [91, np.nan, 85]
 }

df2 = pd.DataFrame(data2)
df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
df2['Science'] = df2['Science'].fillna(df2['Science'].mean())
print(df2)

 
