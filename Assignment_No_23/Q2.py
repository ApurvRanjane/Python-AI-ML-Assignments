# Q2. Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N.

# Input:
# Data = [100000, 200000, 300000, 400000]

# Expected Task:
# For each number N, calculate:
# 1 + 3 + 5 + ... + N

# Expected Output Format:
# Process ID : <PID>
# Input Number : 100000
# Sum of Odd Numbers : 2500000000

import os 
import multiprocessing
import time

def fun(No):
    print("PID is :",os.getpid())
    print("Input Number : ",No)
    sum = 0
    for i in range(1,No+1):
        if(i % 2 != 0):
            sum = sum + i
    print(f"sum of odd numbers upto {No} is : {sum}")
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