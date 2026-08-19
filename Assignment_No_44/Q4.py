#Q4: Display students who scored more than 85 in Science.

import pandas as pd

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