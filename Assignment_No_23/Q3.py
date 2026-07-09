# Q3. Write a Python program that counts how many even numbers exist between 1 and N using Pool.map().

# Input:
# Data = [100000, 200000, 300000, 400000]

# Expected Output Format:
# Process ID : <PID>
# Input Number : 100000
# Even Number Count : 50000

import os 
import multiprocessing
import time

def fun(No):
    print("PID is :",os.getpid())
    print("Input Number : ",No)
    count = 0
    for i in range(1,No+1):
        if(i % 2 == 0):
           count = count + 1
    print(f"count of even numbers upto {No} is : {count}")
    return count

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