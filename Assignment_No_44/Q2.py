# Q2: Use the DataFrame from Q1 and print descriptive statistics using .describe().

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