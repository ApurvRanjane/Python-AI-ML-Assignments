# Q1: Create a DataFrame for student marks and print basic information like shape, columns, and data types.

# data = {
#     'Name': ['Amit', 'Sagar', 'Pooja'],
#     'Math': [85, 90, 78],
#     'Science': [92, 88, 80],
#     'English': [75, 85, 82]
# }

# Note : Consider the same dataset for this as well as next assignment.

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