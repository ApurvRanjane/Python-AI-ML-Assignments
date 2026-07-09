
# Q5. Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.

# Input:
# Data = [10, 15, 20, 25]

# Expected Task:
# For every N, calculate:
# N!

# Expected Output Format:
# Process ID : <PID>
# Input Number : 20
# Factorial : 2432902008176640000

import os 
import multiprocessing
import time

def factorial(No):
    print("PID is :",os.getpid())
    print("Input Number : ",No)
    mul = 1
    for i in range(1,No+1):
        mul = mul*i
    print(f"Factorial of {No} is : {mul}")
    return mul

def main():
    start_time=time.time()
    data = [10,15,20,25]
    result = []
    p = multiprocessing.Pool()
    result = p.map(factorial,data)
    p.close()
    p.join()
    print(result)
    end_time = time.time()
    print("Execution time is : ",end_time-start_time)

if __name__=="__main__":
    main()