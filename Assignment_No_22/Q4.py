# 4. Write a program that calculates:

# 1^5 + 2^5 + 3^5 + ...... + N^5

# for multiple values of N simultaneously using Pool.

# Input:
# [
# 1000000,
# 2000000,
# 3000000,
# 4000000
# ]

# Measure total execution time.

import os 
import multiprocessing
import time

def fun(No):
    print("PID is :",os.getpid())
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i**5)
    return sum 

def main():
    start_time=time.time()
    data = [1000000,2000000, 3000000, 4000000]
    result = []
    p = multiprocessing.Pool()
    result = p.map(fun,data)
    p.close()
    p.join()
    print(result)
    end_time = time.time()
    print("Execution time is : ",end_time-start_time)

if __name__=="__main__":
    main()