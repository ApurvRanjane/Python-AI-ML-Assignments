# 1. Write a Python program that calculates the mean of a dataset using NumPy for the following values:
# [6, 7, 8, 9, 10, 11, 12]

import numpy as np

def main():
    data = [6,7,8,9,10,11,12]

    mean = np.mean(data)

    print("Mean of data is: ",mean)

if __name__== "__main__":
    main()
