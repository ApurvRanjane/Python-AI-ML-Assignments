# 1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

# Example Input:
# [1000000, 2000000, 3000000, 4000000]

# Expected Output:
# [
# 333333833333500000,
# 2666668666667000000,
# ...
# ]
import os 
import multiprocessing
import time

def fun(No):
    print("PID is :",os.getpid())
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i*i)
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