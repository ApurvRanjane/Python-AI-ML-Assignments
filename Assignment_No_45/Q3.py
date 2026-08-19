# Q3: Group students by gender and calculate average marks.

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
