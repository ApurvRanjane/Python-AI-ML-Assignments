# 2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

# Input:
# [10, 15, 20, 25]

# Display:
# • Process ID
# • Input Number
# • Factorial

import os 
import multiprocessing
import time

def factorial(No):
    print("PID is :",os.getpid())
    print("Facorial for : ",No)
    mul = 1
    for i in range(1,No+1):
        mul = mul * i
    return mul 

def main():
    start_time=time.time()
    data = [10, 15, 20, 25]
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